import requests, re, os
from typecho.logic.database import DB

def md5(string):
    import hashlib
    m = hashlib.md5()
    m.update(bytes(string, 'utf-8'))
    return str(m.hexdigest()).lower()


def url_encode(string):
    from urllib.parse import quote
    return quote(string, 'utf-8')


class POST():

    def __init__(self, url, token1, ip, user, password, database):
        self.host_url = url
        self.token1 = token1
        self.ip = ip
        self.user=user 
        self.password = password
        self.database = database
        self.session = requests.Session()
        #self.session_login = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',}
        self.proxies = {'http':'127.0.0.1:8080','https': '127.0.0.1:8080'}
        self.login()

    
    def join_token(self, token4):
        token = self.token1 + '&' + self.token2 + '&' + self.token3 + '&' + token4
        token = md5(token)
        return token


    def login(self):
        #print('####登录后台中####')
        token4 = '{}/admin/login.php?referer={}%2Fadmin%2F'.format(self.host_url, url_encode(self.host_url))
        token = md5(self.token1 + '&' + token4)
        url = self.host_url + '/index.php/action/login?_=%s' % token
        data = {
            'name': 'admin',
            'password': 'DdhjX520',
            'referer': '{}%2Fadmin%2F'.format(url_encode(self.host_url))
            }
        self.headers['Referer'] = token4
        self.session.post(url, data, headers=self.headers)
        #print('Cookies:', self.session.cookies.get_dict())

        self.db = DB(self.ip, self.user, self.password, self.database)    
        self.token2 = str(self.db.user_authCode)
        self.token3 = str(self.db.user_uid)

    
    def write_post(self, title, text, cid='', mid='', date='', attachment=(), img_url='', preview='', h2h3='1'):
        #print('####上传文本####')
        token = self.join_token(r'{}/admin/write-post.php'.format(self.host_url))
        url = self.host_url + '/index.php/action/contents-post-edit?_=%s' % token
        if mid == '':
            self.db.cursor.execute('SELECT value FROM typecho_options WHERE name="defaultCategory";')
            mid = self.db.cursor.fetchone()[0]
        data = {
            'title': title,
            'text': text,
            'fields[thumbnail]': img_url,
            'fields[previewContent]': preview,
            'fields[showTOC]': h2h3,
            'cid': cid,
            'do': 'publish',
            'markdown': '1',
            'date': date,
            'category[]': mid,
            'tags': '',
            'visibility': 'publish',
            'password': '',
            'allowComment': '1',
            'allowPing': '1',
            'allowFeed': '1',
            'trackback': '',
            'attachment[]': attachment,     #元组形式
            'timezone': '28800'
            }
        self.headers['Referer'] = r'{}/admin/write-post.php'.format(self.host_url)
        r = self.session.post(url, data, headers=self.headers)#, proxies=self.proxies)
        return True if r.status_code == 200 else False


    def write_page(self, title, slug, text, cid='', order='', date='', attachment=(), img_url='', preview='', h2h3=''):
        print('####上传文本####')
        token = self.join_token(r'{}/admin/write-page.php'.format(self.host_url))
        url = self.host_url + '/index.php/action/contents-page-edit?_=%s' % token
        data = {
            'title': title,
            'slug': slug, 
            'text': text,
            'fields[thumbnail]': img_url,
            'fields[previewContent]': preview,
            'fields[showTOC]': h2h3,
            'cid': cid,
            'do': 'publish',
            'markdown': '1',
            'date': date,
            'order': order,
            'template': '',
            'visibility': 'publish',
            'allowComment': '1',
            'allowPing': '1',
            'allowFeed': '1',
            'attachment[]': attachment,     #元组形式
            'timezone': '28800'
        }
        self.headers['Referer'] = r'{}/admin/write-page.php'.format(self.host_url)
        r = self.session.post(url, data, headers=self.headers)#, proxies=self.proxies)
        return True if r.status_code == 200 else False


    def delete_post(self, cid):
        token = self.join_token(r'{}/admin/manage-posts.php'.format(self.host_url))
        url = self.host_url + '/index.php/action/contents-post-edit?do=delete&_=%s' % token
        data = {'cid': cid}
        self.headers['Referer'] = r'{}/admin/manage-posts.php'.format(self.host_url)
        r = self.session.post(url, data, headers=self.headers)#, proxies=self.proxies)
        return True if r.status_code == 200 else False

    
    def delete_page(self, cid):
        token = self.join_token(r'{}/admin/manage-pages.php'.format(self.host_url))
        url = self.host_url + '/index.php/action/contents-page-edit?do=delete&_=%s' % token
        data = {'cid': cid}
        self.headers['Referer'] = r'{}/admin/manage-pages.php'.format(self.host_url)
        r = self.session.post(url, data, headers=self.headers)#, proxies=self.proxies)
        return True if r.status_code == 200 else False


    def do_meta(self, do, name, slug, parent=0, description='', mid=''):
        '''
        return n    创建成功,mid为n
        return -1   分类名称已经存在
        return -2   缩略名已经存在
        return -3   二者都已存在
        return -4   未知错误
        '''
        token = self.join_token(r'{}/admin/category.php'.format(self.host_url))
        url = self.host_url + '/index.php/action/metas-category-edit?_=%s' % token
        data = {
            'name': name,
            'slug': slug,
            'parent': parent,
            'description': description,
            'do': do,
            'mid': mid
        }
        self.headers['Referer'] = r'{}/admin/category.php'.format(self.host_url)
        r = self.session.post(url, data, headers=self.headers)
        if '分类名称已经存在' in r.text and '缩略名已经存在' in r.text:
            return -3
        elif '分类名称已经存在' not in r.text and '缩略名已经存在' in r.text:
            return -2
        elif '分类名称已经存在' in r.text and '缩略名已经存在' not in r.text:
            return -1
        else:
            self.db.cursor.execute('SELECT mid FROM typecho_metas WHERE name="%s";' % name)
            mid = self.db.cursor.fetchone()
            if mid:
                return mid[0]
            else:
                return -4


    def delete_meta(self, merge, mid):
        #merge为要删除的分类所在的那一层的第一个分类的mid
        if merge == 0:
            self.db.cursor.execute('SELECT value FROM typecho_options WHERE name="defaultCategory";')
            merge = self.db.cursor.fetchone()[0]

        token = self.join_token(r'{}/admin/manage-categories.php'.format(self.host_url))
        url = self.host_url + '/index.php/action/metas-category-edit?do=delete&_=%s' % token
        data = {
            'merge': merge,
            'mid[]': mid
        }
        self.headers['Referer'] = r'{}/admin/manage-categories.php'.format(self.host_url)
        r = self.session.post(url, data, headers=self.headers)
        return True if r.status_code == 200 else False


    def upload_attachment(self, pic_path, name='', cid=''):    
        '''
        return img{'url': %s, 'cid': %d}
        PS: name要带后缀，否则上传失败
        '''
        #print('####正在上传%s####'%pic_path)
        if name == '':
            name = os.path.split(pic_path)[1]
        name = url_encode(name)
        token = self.join_token(r'{}/admin/write-post.php'.format(self.host_url))
        if cid == '':
            url = self.host_url + '/index.php/action/upload?_=%s' % token
        else:
            url = self.host_url + '/index.php/action/upload?cid=%d&_=%s' % (cid, token)
        data = {'name': name}
        files = {'file': (name, open(pic_path, 'rb'))}
        self.headers['Referer'] = r'{}/admin/write-post.php'.format(self.host_url)
        r = self.session.post(url, data, files=files, headers=self.headers)
        img = {
            'url': r.json()[0],
            'cid': r.json()[1]['cid']
        }
        return img