# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from typecho.logic.operation import Operation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 575)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 243, 546))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView_metas = QtWidgets.QListView(self.tab)
        self.listView_metas.setGeometry(QtCore.QRect(-1, -1, 241, 523))
        self.listView_metas.setObjectName("listView_metas")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 20, 641, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView_passages = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView_passages.setObjectName("listView_passages")
        self.horizontalLayout.addWidget(self.listView_passages)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 480, 641, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_create_post = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_create_post.setObjectName("pushButton_create_post")
        self.gridLayout.addWidget(self.pushButton_create_post, 0, 0, 1, 1)
        self.pushButton_update_post_fast = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_update_post_fast.setObjectName("pushButton_update_post_fast")
        self.gridLayout.addWidget(self.pushButton_update_post_fast, 2, 0, 1, 1)
        self.pushButton_update_post = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_update_post.setObjectName("pushButton_update_post")
        self.gridLayout.addWidget(self.pushButton_update_post, 1, 0, 1, 1)
        self.pushButton_create_page = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_create_page.setObjectName("pushButton_create_page")
        self.gridLayout.addWidget(self.pushButton_create_page, 0, 1, 1, 1)
        self.pushButton_update_page = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_update_page.setObjectName("pushButton_update_page")
        self.gridLayout.addWidget(self.pushButton_update_page, 1, 1, 1, 1)
        self.pushButton_update_page_fast = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_update_page_fast.setObjectName("pushButton_update_page_fast")
        self.gridLayout.addWidget(self.pushButton_update_page_fast, 2, 1, 1, 1)
        self.pushButton_create_meta = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_create_meta.setObjectName("pushButton_create_meta")
        self.gridLayout.addWidget(self.pushButton_create_meta, 0, 2, 1, 1)
        self.pushButton_update_meta = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_update_meta.setObjectName("pushButton_update_meta")
        self.gridLayout.addWidget(self.pushButton_update_meta, 1, 2, 1, 1)
        self.pushButton_delete_meta = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_delete_meta.setObjectName("pushButton_delete_meta")
        self.gridLayout.addWidget(self.pushButton_delete_meta, 2, 2, 1, 1)
        self.pushButton_download_with_img = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_download_with_img.setObjectName("pushButton_download_with_img")
        self.gridLayout.addWidget(self.pushButton_download_with_img, 2, 3, 1, 1)
        self.pushButton_download_and_open = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_download_and_open.setObjectName("pushButton_download_and_open")
        self.gridLayout.addWidget(self.pushButton_download_and_open, 1, 3, 1, 1)
        self.pushButton_download = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_download.setObjectName("pushButton_download")
        self.gridLayout.addWidget(self.pushButton_download, 0, 3, 1, 1)
        self.pushButton_settings = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.gridLayout.addWidget(self.pushButton_settings, 2, 5, 1, 1)
        self.pushButton_backups_all = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_backups_all.setObjectName("pushButton_backups_all")
        self.gridLayout.addWidget(self.pushButton_backups_all, 1, 5, 1, 1)
        self.pushButton_delete_passage = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_delete_passage.setObjectName("pushButton_delete_passage")
        self.gridLayout.addWidget(self.pushButton_delete_passage, 2, 4, 1, 1)
        self.pushButton_open_file = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.gridLayout.addWidget(self.pushButton_open_file, 0, 4, 1, 1)
        self.pushButton_open_dir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_open_dir.setObjectName("pushButton_open_dir")
        self.gridLayout.addWidget(self.pushButton_open_dir, 1, 4, 1, 1)
        self.pushButton_open_url = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_open_url.setObjectName("pushButton_open_url")
        self.gridLayout.addWidget(self.pushButton_open_url, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 3, 26, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_no_meta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_no_meta.setGeometry(QtCore.QRect(30, 549, 75, 23))
        self.pushButton_no_meta.setObjectName("pushButton_no_meta")
        self.pushButton_list_pages = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_list_pages.setGeometry(QtCore.QRect(140, 549, 75, 23))
        self.pushButton_list_pages.setObjectName("pushButton_list_pages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.not_qt_creater()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typecho博客管理姬   --by iyzyi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "分类"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "标签"))
        self.pushButton_create_post.setText(_translate("MainWindow", "创建文章"))
        self.pushButton_update_post_fast.setText(_translate("MainWindow", "快速更新文章"))
        self.pushButton_update_post.setText(_translate("MainWindow", "更新文章"))
        self.pushButton_create_page.setText(_translate("MainWindow", "创建独立页面"))
        self.pushButton_update_page.setText(_translate("MainWindow", "更新独立页面"))
        self.pushButton_update_page_fast.setText(_translate("MainWindow", "快速更新独立页面"))
        self.pushButton_create_meta.setText(_translate("MainWindow", "创建分类"))
        self.pushButton_update_meta.setText(_translate("MainWindow", "更新分类"))
        self.pushButton_delete_meta.setText(_translate("MainWindow", "删除分类"))
        self.pushButton_download_with_img.setText(_translate("MainWindow", "下载含图片"))
        self.pushButton_download_and_open.setText(_translate("MainWindow", "下载并打开"))
        self.pushButton_download.setText(_translate("MainWindow", "下载内容"))
        self.pushButton_settings.setText(_translate("MainWindow", "客户端配置"))
        self.pushButton_backups_all.setText(_translate("MainWindow", "全站备份"))
        self.pushButton_delete_passage.setText(_translate("MainWindow", "删除文章"))
        self.pushButton_open_file.setText(_translate("MainWindow", "打开文件"))
        self.pushButton_open_dir.setText(_translate("MainWindow", "打开缓存目录"))
        self.pushButton_open_url.setText(_translate("MainWindow", "打开网页"))
        self.label.setText(_translate("MainWindow", "文章"))
        self.pushButton_no_meta.setText(_translate("MainWindow", "无分类"))
        self.pushButton_list_pages.setText(_translate("MainWindow", "独立页面"))


    def not_qt_creater(self):
        self.list_metas()
        self.list_posts(0)
        self.pushButton_list_pages.clicked.connect(self.list_pages)
        self.pushButton_no_meta.clicked.connect(self.list_no_meta_posts)


    def list_metas(self):
        self.operation = Operation()
        self.metas_detail_list = self.operation.get_metas()
        self.metas_name_list = [meta['name'] for meta in self.metas_detail_list]

        self.slm = QtCore.QStringListModel();
        self.slm.setStringList(self.metas_name_list)
        self.listView_metas.setModel(self.slm)
        self.listView_metas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_metas.clicked.connect(self.clicked_meta)
        

    def list_passages(self, passages_detail_list):
        self.passages_detail_list = passages_detail_list
        self.passages_title_list = [passage['title'] for passage in self.passages_detail_list]
        slm = QtCore.QStringListModel()
        slm.setStringList(self.passages_title_list)
        self.listView_passages.setModel(slm)
        self.listView_passages.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  #禁止双击编辑文本

        
    def list_posts(self, mid):
        self.posts_detail_list = self.operation.get_posts(mid)
        #print(self.posts_detail_list)
        self.list_passages(self.posts_detail_list)
        self.list_info = 'posts'


    def list_no_meta_posts(self):
        self.list_metas()
        self.no_meta_posts = self.operation.get_no_meta_posts()
        self.list_passages(self.no_meta_posts)
        self.list_info = 'posts'


    def list_pages(self):
        self.list_metas()
        self.pages_detail_list = self.operation.get_pages()
        self.list_passages(self.pages_detail_list)
        self.list_info = 'pages'


    def clicked_meta(self, qModelIndex):
        mid = self.metas_detail_list[qModelIndex.row()]['mid']
        self.list_posts(mid)
    

    def cancel_selected_meta(self): #选中分类时点击创建独立页面，创建完成后文章列表显示独立页面，但是分类列表依然选中分类，不美观
        pass


'''
self.metas_name_list            分类名列表
self.metas_detail_list          分类列表，元素为字典dict = {'title': title, 'cid': cid, 'mid': mid, 'created': date}
self.passages_title_list         文章名列表
self.passages_detail_list       文章列表，元素为字典dict = {'title': title, 'mid': mid, 'date': date, 'img_url': img_url, 'preview': preview, 'h2h3': h2h3}

self.pages_detail_list
'''


'''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
'''