import os, re, requests, json
from typecho.logic.database import DB
from typecho.logic.post import POST
from typecho.logic.img import IMG


class Typecho():

    def __init__(self, user_dict):
        self.url = user_dict['url']
        self.token1 = user_dict['token1']
        self.ip = user_dict['ip']
        self.user = user_dict['user']
        self.password = user_dict['password']
        self.database = user_dict['database']
        self.localDir = user_dict['localDir']
        self.login_user = user_dict['login_user']
        self.login_password = user_dict['login_password']
        if not os.path.exists(self.localDir):
            os.makedirs(self.localDir)
        
        self.db = DB(ip=self.ip, user=self.user, password=self.password, database=self.database)
        self.post = POST(self.url, self.token1, self.ip, self.user, self.password, self.database, self.login_user, self.login_password)


    def write_post(self, title, text, cid='', mid='', date='', img_url='', preview='', h2h3=''):
        try:
            img = IMG(self.post, text, self.url, self.localDir, cover_img_url=img_url)
            img_list = img.get_upload_img_list()
            text = img.img_sub()
        except Exception as e:
            raise RuntimeError('图片正则替换出错！')

        if img_url != '':
            info = img.upload_cover_img()
            img_url, cover_img_cid = info['url'], info['cid']
            attachment = tuple([img['cid'] for img in img_list] + [cover_img_cid])
        else:
            attachment = tuple([img['cid'] for img in img_list])

        return self.post.write_post(title, text, cid=cid, mid=mid, date=date, attachment=attachment, img_url=img_url, preview=preview, h2h3=h2h3)


    def write_page(self, title, slug, text, cid='', date='', img_url='', preview='', h2h3=''):
        try:
            img = IMG(self.post, text, self.url, self.localDir, cover_img_url=img_url)
            img_list = img.get_upload_img_list()
            text = img.img_sub()
        except Exception as e:
            raise RuntimeError('图片正则替换出错！')

        if img_url != '':
            info = img.upload_cover_img()
            img_url, cover_img_cid = info['url'], info['cid']
            attachment = tuple([img['cid'] for img in img_list] + [cover_img_cid])
        else:
            attachment = tuple([img['cid'] for img in img_list])

        if cid != '':
            self.db.cursor.execute('SELECT `order` from typecho_contents WHERE cid=%d;' % cid)
            order = self.db.cursor.fetchone()[0]
        else:
            order = ''
        return self.post.write_page(title, slug, text, cid=cid, order=order, date=date, attachment=attachment, img_url=img_url, preview=preview, h2h3=h2h3)


    def delete_post(self, cid):
        return self.post.delete_post(cid)


    def delete_page(self, cid):
        return self.post.delete_post(cid)

    '''
    def edit_passage(self, title, text, cid, mid='', date=''):
        img = IMG(self.post, text, self.url, self.localDir)
        img_dict = img.upload_img()
        text = img.img_sub()
        attachment = tuple([img['cid'] for img in img_dict])
        if mid == '':
            self.db.cursor.execute('SELECT mid FROM typecho_contents WHERE cid=%d;' % cid)
            mid = self.db.cursor.fetchone()[0]
        self.post.write_post(title, text, cid=cid, mid=mid, date=date, attachment=attachment)
    '''

    def do_meta(self, do, name, slug, parent, description, mid=''):
        return self.post.do_meta(do, name, slug, parent, description, mid)
    

    def delete_meta(self, merge, mid):
        return self.post.delete_meta(merge, mid)


    def get_passage(self, cid):
        self.db.cursor.execute('SELECT title,text FROM typecho_contents WHERE cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        title = info[0]
        text = info[1]
        text = re.sub(r'<!--markdown-->', '', text)
        text = re.sub(r'\r\n', r'\n', text)
        file_path = os.path.join(self.localDir, title+'.md')
        with open(file_path, 'w', encoding='utf-8',errors='ignore') as f:
            f.write(text)
        return title

    
    def get_metas(self):
        self.db.cursor.execute('SELECT name,mid,parent,`order` FROM typecho_metas;') #MySQL关键字作为列名表名的处理方式
        metas_info = self.db.cursor.fetchall()
        metas_list = [{'name': '所有文章', 'mid': 0, 'parent': -1, 'order': 0}]
        for meta in metas_info:
            dict = {
                'name': meta[0],
                'mid': meta[1],
                'parent': meta[2],
                'order': meta[3]
            }
            metas_list.append(dict)
        
        self.metas_list = []
        def dg(parent, deep):
            son = [meta for meta in metas_list if meta['parent'] == parent]
            son.sort(key = lambda meta: meta['order'])
            for meta in son:
                meta['name'] = '　' * deep + meta['name']
                self.metas_list.append(meta)
                dg(meta['mid'], deep+1)
        dg(-1, 0)
        return self.metas_list
        

    def get_posts(self, mid=0):
        if mid == 0:
            self.db.cursor.execute('SELECT title,cid,created FROM typecho_contents WHERE type="post";') #MySQL关键字作为列名表名的处理方式
            passages_info = self.db.cursor.fetchall()
            self.passages_list = []
            for passage in passages_info:
                dict = {
                    'title': passage[0],
                    'cid': passage[1],
                    'mid': mid,
                    'created': passage[2]
                }
                self.passages_list.append(dict)
        else:
            self.db.cursor.execute('SELECT mid,parent FROM typecho_metas;')
            metas = self.db.cursor.fetchall()
            children = [mid]
            def dg(parent):
                nonlocal children
                son = [meta[0] for meta in metas if meta[1] == parent]
                children += son
                for mid in son:
                    dg(mid)
            dg(mid)

            mid_str = 'mid='+ ' or mid='.join(list(map(str, children)))
            self.db.cursor.execute('SELECT cid FROM typecho_relationships WHERE %s;' % mid_str) #MySQL关键字作为列名表名的处理方式
            cids = [cid[0] for cid in self.db.cursor.fetchall()]
            self.passages_list = []
            for cid in cids:
                self.db.cursor.execute('SELECT title,created FROM typecho_contents WHERE cid=%d' % cid)
                passage = self.db.cursor.fetchone()
                dict = {
                    'title': passage[0],
                    'cid': cid,
                    'mid': mid,
                    'created': passage[1]
                }
                self.passages_list.append(dict)
        self.passages_list.sort(key = lambda passage: passage['created'])
        return self.passages_list


    def get_no_meta_posts(self):
        self.db.cursor.execute('SELECT cid FROM typecho_contents WHERE type="post";')
        info = self.db.cursor.fetchall()
        cids = [cid[0] for cid in info]
        no_metas_posts_cids = []
        for cid in cids:
            self.db.cursor.execute('SELECT mid FROM typecho_relationships WHERE cid=%d;' % cid)
            info = self.db.cursor.fetchone()
            if not info:
                no_metas_posts_cids.append(cid)
        self.no_metas_posts_list = []
        for cid in no_metas_posts_cids:
            self.db.cursor.execute('SELECT title,created FROM typecho_contents WHERE cid=%d;' % cid)
            info = self.db.cursor.fetchone()
            dict = {
                'title': info[0],
                'cid': cid,
                'created': info[1]
            }
            self.no_metas_posts_list.append(dict)
        self.no_metas_posts_list.sort(key = lambda post: post['created'])
        return self.no_metas_posts_list


    def get_pages(self):
        self.db.cursor.execute('SELECT title,cid,slug,`order` FROM typecho_contents WHERE type="page";')
        pages_info = self.db.cursor.fetchall()
        self.pages_list = []
        for page in pages_info:
            dict = {
                'title': page[0],
                'cid': page[1],
                'slug': page[2],
                'order': page[3]
            }
            self.pages_list.append(dict)
        self.pages_list.sort(key = lambda page: page['order'])
        return self.pages_list


    def get_post_info(self, cid):
        self.db.cursor.execute('SELECT title,created FROM typecho_contents WHERE cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        title, date = info[0], info[1]
        from time import localtime, strftime
        date = strftime('%Y-%m-%d %H:%M', localtime(date))
        
        self.db.cursor.execute('SELECT mid FROM typecho_relationships WHERE cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        mid = info[0] if info else ''

        self.db.cursor.execute('SELECT str_value FROM typecho_fields WHERE name="thumbnail" and cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        img_url = info[0] if info else ''
            
        self.db.cursor.execute('SELECT str_value FROM typecho_fields WHERE name="previewContent" and cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        preview = info[0] if info else ''

        self.db.cursor.execute('SELECT str_value FROM typecho_fields WHERE name="showTOC" and cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        h2h3 = info[0] if info else ''

        dict = {
            'title': title,
            'mid': mid,
            'date': date,
            'img_url': img_url,
            'preview': preview,
            'h2h3': h2h3
        }
        #print(dict)
        return dict

    def get_meta_info(self, mid):
        self.db.cursor.execute('SELECT name,slug,description,parent FROM typecho_metas WHERE mid=%d;' % mid)
        info = self.db.cursor.fetchone()
        name, slug, description, parent = info[0], info[1], info[2], info[3]
        dict = {
            'mid': mid,
            'name': name,
            'slug': slug,
            'description': description,
            'parent': parent
        }
        return dict

    def get_page_info(self, cid):
        self.db.cursor.execute('SELECT title,slug,created FROM typecho_contents WHERE cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        title, slug, date = info[0], info[1], info[2]
        from time import localtime, strftime
        date = strftime('%Y-%m-%d %H:%M', localtime(date))

        self.db.cursor.execute('SELECT str_value FROM typecho_fields WHERE name="thumbnail" and cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        img_url = info[0] if info else ''
            
        self.db.cursor.execute('SELECT str_value FROM typecho_fields WHERE name="previewContent" and cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        preview = info[0] if info else ''

        self.db.cursor.execute('SELECT str_value FROM typecho_fields WHERE name="showTOC" and cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        h2h3 = info[0] if info else ''

        dict = {
            'cid': cid,
            'title': title,
            'slug': slug,
            'date': date,
            'img_url': img_url,
            'preview': preview,
            'h2h3': h2h3
        }
        return dict


    def download_passage_with_img(self, cid):
        self.db.cursor.execute('SELECT title,text FROM typecho_contents WHERE cid=%d;' % cid)
        info = self.db.cursor.fetchone()
        title = info[0]
        text = info[1]
        text = re.sub(r'<!--markdown-->', '', text)
        text = re.sub(r'\r\n', r'\n', text)

        img = IMG(self.post, text, self.url, self.localDir)
        img_list = img.get_download_img_list()
        text = img.img_sub()

        file_path = os.path.join(self.localDir, title+'.md')
        with open(file_path, 'w', encoding='utf-8',errors='ignore') as f:
            f.write(text)
        return title

    
    def get_all_cids_with_title(self):
        self.db.cursor.execute('SELECT cid,title FROM typecho_contents WHERE type="post" or type="page";')
        list = self.db.cursor.fetchall()
        return [{'cid': passage[0], 'title': passage[1]} for passage in list]