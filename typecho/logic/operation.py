import os, json
from typecho.logic.typecho import Typecho
from PyQt5.QtWidgets import QMessageBox
from collections import OrderedDict

class Operation():

    def __init__(self):
        self.typecho_init()


    def typecho_init(self):
        if self.exists_settings():
            choose_blog_num, blogs_list = self.get_settings_info()
            choose_blog = blogs_list[choose_blog_num]
            #print(choose_blog)
            self.typecho = Typecho(choose_blog)
        else:
            QMessageBox.information(None, '错误', '没有配置文件！', QMessageBox.Ok, QMessageBox.Ok)


    def exists_settings(self):
        return True if os.path.exists(r'.\typecho.conf') else False


    def get_settings_info(self):
        with open(r'.\typecho.conf', 'r', encoding='utf-8') as f:
            file = f.read()
        conf_list = json.loads(file)
        choose_blog_num = conf_list[0]['choose']
        blogs_list = conf_list[1]
        for n, blog in enumerate(blogs_list):
            blog['num'] = n
        return choose_blog_num, blogs_list


    def get_ordered_dict(self, dict):
        return OrderedDict([('url', dict['url']), ('token1', dict['token1']), ('ip', dict['ip']), ('user', dict['user']), ('password', dict['password']), ('database', dict['database']), ('localDir', dict['localDir'])]) 


    def add_blog_setting(self, blog_detail_list):
        with open(r'.\typecho.conf', 'r', encoding='utf-8') as f:
            file = f.read()
        conf_list = json.loads(file)
        conf_list[1].append(blog_detail_list)
        for i, dict in enumerate(conf_list[1]):
            conf_list[1][i] = self.get_ordered_dict(conf_list[1][i])
        conf_json = json.dumps(conf_list, indent=4, separators=(',', ':'), ensure_ascii=False, sort_keys=False)
        with open(r'.\typecho.conf', 'w', encoding='utf-8') as f:
            f.write(conf_json)


    def update_blog_setting(self, choose_blog_num, blog_detail_list):
        with open(r'.\typecho.conf', 'r', encoding='utf-8') as f:
            file = f.read()
        conf_list = json.loads(file)
        conf_list[1][choose_blog_num] = blog_detail_list
        for i, dict in enumerate(conf_list[1]):
            conf_list[1][i] = self.get_ordered_dict(conf_list[1][i])
        conf_json = json.dumps(conf_list, indent=4, separators=(',', ':'), ensure_ascii=False, sort_keys=False)
        with open(r'.\typecho.conf', 'w', encoding='utf-8') as f:
            f.write(conf_json)


    def choose_blog_setting(self, choose_blog_num):
        with open(r'.\typecho.conf', 'r', encoding='utf-8') as f:
            file = f.read()
        conf_list = json.loads(file)
        conf_list[0]['choose'] = choose_blog_num
        conf_json = json.dumps(conf_list, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
        with open(r'.\typecho.conf', 'w', encoding='utf-8') as f:
            f.write(conf_json)
        QMessageBox.information(None, '选择博客', '选择博客：%s' % conf_list[1][choose_blog_num], QMessageBox.Ok, QMessageBox.Ok)
    

    def write_post(self, filepath, title, meta, date, img_url, preview, h2h3, cid=''):
        with open(filepath, 'r', encoding='utf-8')as f:
            text = f.read()
        return self.typecho.write_post(title, text, cid=cid, mid=meta, date=date, img_url=img_url, preview=preview, h2h3=h2h3)


    def delete_post(self, cid):
        return self.typecho.delete_post(cid)

    def delete_page(self, cid):
        return self.typecho.delete_page(cid)


    def create_page(self, filepath, title, slug, date='', img_url='', preview='', h2h3=''):
        with open(filepath, 'r', encoding='utf-8')as f:
            text = f.read()        
        return self.typecho.write_page(title, slug, text, cid='', date=date, img_url=img_url, preview=preview, h2h3=h2h3)


    def update_page(self, filepath, title, slug, cid, date='', img_url='', preview='', h2h3=''):
        with open(filepath, 'r', encoding='utf-8')as f:
            text = f.read()        
        return self.typecho.write_page(title, slug, text, cid, date=date, img_url=img_url, preview=preview, h2h3=h2h3)


    def get_metas(self):
        return self.typecho.get_metas()

    def get_posts(self, mid):
        return self.typecho.get_posts(mid)

    def get_no_meta_posts(self):
        return self.typecho.get_no_meta_posts()

    def get_pages(self):
        return self.typecho.get_pages()

    def get_meta_info(self, mid):
        return self.typecho.get_meta_info(mid)

    def get_post_info(self, cid):
        return self.typecho.get_post_info(cid)

    def get_page_info(self, cid):
        return self.typecho.get_page_info(cid)

    
    def create_meta(self, name, slug, parent, description):
        return self.typecho.do_meta('insert', name, slug, parent, description)


    def update_meta(self, name, slug, parent, description, mid):
        return self.typecho.do_meta('update', name, slug, parent, description, mid=mid)


    def delete_meta(self, metas_detail_list, row):
        #print(row, metas_detail_list[row])
        parent_row = -1
        for i, meta in enumerate(metas_detail_list):
            if meta['mid'] == metas_detail_list[row]['parent']:
                parent_row = i
                break
        merge = metas_detail_list[parent_row+1]['mid']
        mid = metas_detail_list[row]['mid']   
        #print('merge: %d %s\nmid: %d %s'%(merge, metas_detail_list[parent_row+1]['name'], mid, metas_detail_list[row]['name']))2
        return self.typecho.delete_meta(merge, mid)

    
    def update_post_fast(self, cid):
        dict = self.get_post_info(cid)
        title, meta, date, img_url, preview, h2h3 = dict['title'], dict['mid'], dict['date'], dict['img_url'], dict['preview'], dict['h2h3']
        file_path = os.path.join(self.typecho.localDir, title+'.md')
        if not os.path.exists(file_path):
            QMessageBox.warning(None, '快速更新文章', '缓存目录下无文件：\n%s' % title+'.md', QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                r = self.write_post(file_path, title, meta, date, img_url, preview, h2h3, cid=cid)
            except Exception as e:
                QMessageBox.warning(None, '快速更新文章', '程序运行错误！\n%s'%str(e), QMessageBox.Ok, QMessageBox.Ok)
            else:
                if not r:
                    QMessageBox.warning(None, '快速更新文章', '快速更新文章失败！', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.information(None, '快速更新文章', '快速更新文章成功！', QMessageBox.Ok, QMessageBox.Ok)
    

    def update_page_fast(self, cid):
        dict = self.get_page_info(cid)
        title, slug, date, img_url, preview, h2h3 = dict['title'], dict['slug'], dict['date'], dict['img_url'], dict['preview'], dict['h2h3']
        file_path = os.path.join(self.typecho.localDir, title+'.md')
        if not os.path.exists(file_path):
            QMessageBox.warning(None, '快速更新独立页面', '缓存目录下无文件：\n%s' % title+'.md', QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                r = self.update_page(file_path, title, slug, cid, date=date, img_url=img_url, preview=preview, h2h3=h2h3)
            except Exception as e:
                QMessageBox.warning(None, '快速更新独立页面', '程序运行错误！\n%s'%str(e), QMessageBox.Ok, QMessageBox.Ok)
            else:
                if not r:
                    QMessageBox.warning(None, '快速更新独立页面', '快速更新独立页面失败！', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.information(None, '快速更新独立页面', '快速更新独立页面成功！', QMessageBox.Ok, QMessageBox.Ok)


    def download_passage(self, cid):
        try:
            self.typecho.get_passage(cid)
        except Exception as e:
            QMessageBox.warning(None, '下载文章', '程序运行错误！\n%s'%str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(None, '下载文章', '下载文章成功！', QMessageBox.Ok, QMessageBox.Ok)


    def download_and_open_passage(self, cid):
        try:
            title = self.typecho.get_passage(cid)
        except Exception as e:
            QMessageBox.warning(None, '下载并打开', '程序运行错误！\n%s'%str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.open_file(title)


    def download_passage_with_img(self, cid):
        try:
            self.typecho.download_passage_with_img(cid)
        except Exception as e:
            QMessageBox.warning(None, '下载文章（含图片）', '程序运行错误！\n%s'%str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(None, '下载文章（含图片）', '下载文章（含图片）成功！', QMessageBox.Ok, QMessageBox.Ok)


    def open_file(self, title):
        path = self.typecho.localDir
        file_path = os.path.join(path, title+'.md')
        if os.path.exists(file_path):
            os.system('start explorer "%s"' % file_path)
        else:
            QMessageBox.warning(None, '提示', '缓存目录下无文件：\n%s' % title+'.md', QMessageBox.Ok, QMessageBox.Ok)


    def open_dir(self):
        path = self.typecho.localDir
        if os.path.exists(path):
            os.system('start explorer "%s"' % path)
        else:
            QMessageBox.warning(None, '提示', '缓存目录不存在！', QMessageBox.Ok, QMessageBox.Ok)
        
    
    def get_all_cids_with_title(self):
        return self.typecho.get_all_cids_with_title()
     

if __name__ == '__main__':
    o = Operation()
    #o.list_metas()
    o.list_passages(12)