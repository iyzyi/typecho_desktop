import re, os, requests

class IMG():

    def __init__(self, post, text, host_url, dir_path, cid='', cover_img_url=''):
        self.post = post
        self.text = text
        self.host_url = host_url
        self.dir_path = dir_path
        self.img_dir_path = os.path.join(dir_path, 'img')
        if not os.path.exists(self.img_dir_path):
            os.makedirs(self.img_dir_path)
        self.cid = cid
        self.cover_img_url = cover_img_url
        self.img_infos = []
        self.img_find()


    def text_except_code(self):
        #去除文本中的`代码段`，以便提取图片（代码段中的图片链接不提取出来）
        text = re.sub(r'```.*?\n.+?\n```', '', self.text, flags=re.DOTALL)
        text = re.sub(r'`[^`]+?`', '', text)
        return text


    def img_find(self):
        '''
        return list of img links
        '''
        
        self.text2 = self.text_except_code()

        img_list = re.findall(r'\!\[.*?\]\((.*?\.(?:jpg|png|gif|bmp|jpeg|tiff))\)', self.text2)
        
        flags = re.findall(r'\!\[.*?\]\[(.+?)\]', self.text)
        links = re.findall(r'\[(.+?)\]: *?(.*?\.(?:jpg|png|gif|bmp|jpeg|tiff))', self.text2)
        for link in links:
            for flag in flags:
                if flag == link[0]:
                    img_list.append(link[1].strip())
        
        img_list = [re.sub(r'^file:///(?=[a-zA-Z]:(\\|/))', '', img) for img in img_list]  #有道云文章中的部分图片
        self.img_list = [{'front': img} for img in img_list]


    def download_img(self, url, path):
        #print('####正在下载%s####'%url)
        r = requests.get(url)
        if r:
            name = os.path.split(url)[1]
            pic_path = os.path.join(path, name)
            with open(pic_path, 'wb') as f:
                f.write(r.content)
            return pic_path
        else:
            #print('####下载失败%s####'%url)
            pass


    def get_upload_img_list(self):
        no_need = []
        for img in self.img_list:

            if re.search(r'^[a-zA-Z]:(\\|/)', img['front']):     #本地图片绝对路径
                img['middle'] = img['front']
                if self.cid == '':
                    info = self.post.upload_attachment(img['middle'])
                    img['back'] = info['url']
                    img['cid'] = info['cid']
                else:
                    info = self.post.upload_attachment(img['middle'], cid=self.cid)
                    img['back'] = info['url']
                    img['cid'] = info['cid']
            
            elif re.search(r'^\.\\img', img['front']):           #本地图片相对路径
                img['middle'] = re.sub(r'^\.', self.dir_path.replace('\\','\\\\'), img['front'])
                if self.cid == '':
                    info = self.post.upload_attachment(img['middle'])
                    img['back'] = info['url']
                    img['cid'] = info['cid']
                else:
                    info = self.post.upload_attachment(img['middle'], cid=self.cid)
                    img['back'] = info['url']
                    img['cid'] = info['cid']
            
            elif re.search(r'^https?://', img['front']):        #网络图片
                if re.search('^%s/usr/uploads/'%self.host_url.replace('.','\\.'), img['front']):    #本站的网络图片
                    no_need.append(img)
                else:                                           #非本站的网络图片
                    img['middle'] = self.download_img(img['front'], self.img_dir_path)
                    if self.cid == '':
                        info = self.post.upload_attachment(img['middle'])
                        img['back'] = info['url']
                        img['cid'] = info['cid']
                    else:
                        info = self.post.upload_attachment(img['middle'], cid=self.cid)
                        img['back'] = info['url']
                        img['cid'] = info['cid']
        
        for img in no_need:                                     #不要在迭代过程中使用remove()                             
            self.img_list.remove(img)
        return self.img_list


    def get_download_img_list(self):
        no_need = []
        for img in self.img_list:
            if re.search(r'^https?://', img['front']):
                img['middle'] = self.download_img(img['front'], self.img_dir_path)
                img['back'] = img['middle'].replace(self.dir_path, '.') #改为相对路径
            else:
                no_need.append(img)
        for img in no_need:
            self.img_list.remove(img)
        return self.img_list
    

    def img_sub(self):
        #print(self.img_list)
        for img in self.img_list:
            img['front'] = img['front'].replace('\\', '\\\\')
            img['back'] = img['back'].replace('\\','\\\\')
            rs = r'*.?+$^[](){}|/'
            for i in rs: 
                img['front'] = img['front'].replace(i, '\\'+i)
            self.text = re.sub(r'(\!\[.*?\]\(){}(\))'.format(img['front']), r'\1{}\2'.format(img['back']), self.text)
            self.text = re.sub(r'(\!\[.*?\]\[(.*?)\].*?\[\2\]: *?){}'.format(img['front']), r'\1{}'.format(img['back']), self.text, flags=re.DOTALL)
        return self.text


    def upload_cover_img(self):
        '''
        return dict, key:url,cid
        '''
        if re.search(r'^https?://', self.cover_img_url):
            img_path = self.download_img(self.cover_img_url, self.img_dir_path)
        else:
            img_path = self.cover_img_url
        if self.cid == '':
            info = self.post.upload_attachment(img_path)
        else:
            info = self.post.upload_attachment(img_path, self.cid)
        #print(info)
        return info