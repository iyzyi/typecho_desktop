# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow, QVBoxLayout, QDialog, QMessageBox
from PyQt5.QtCore import QStringListModel, pyqtSignal

from typecho.logic.operation import Operation
from typecho.gui.mainwindow import Ui_MainWindow
from typecho.gui.create_post import Ui_create_post
from typecho.gui.update_post import Ui_update_post
from typecho.gui.create_meta import Ui_create_meta
from typecho.gui.update_meta import Ui_update_meta
from typecho.gui.create_page import Ui_create_page
from typecho.gui.update_page import Ui_update_page
from typecho.gui.settings import Ui_settings
from typecho.gui.backups_all import Ui_backups_all


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        
class Create_post(QMainWindow, Ui_create_post):
    def __init__(self, parent=None):
        super(Create_post, self).__init__(parent)
        self.setupUi(self)

    def pass_value(self, metas_detail_list):
        self.metas_detail_list = metas_detail_list
        self.metas_detail_list[0]['name'] = '真正的默认分类'
        self.metas_name_list = [meta['name'] for meta in self.metas_detail_list]

    def open(self, metas_detail_list, row):
        self.pass_value(metas_detail_list)
        self.comboBox_metas.clear()
        self.comboBox_metas.addItems(self.metas_name_list)
        self.comboBox_metas.setCurrentIndex(-1) if row == 0 else self.comboBox_metas.setCurrentIndex(row)
        self.show()


class Update_post(QMainWindow, Ui_update_post):
    def __init__(self, parent=None):
        super(Update_post, self).__init__(parent)
        self.setupUi(self)

    def pass_value(self, metas_detail_list):
        self.metas_detail_list = metas_detail_list
        self.metas_name_list = [meta['name'] for meta in self.metas_detail_list]

    def open(self, metas_detail_list, cid):
        self.pass_value(metas_detail_list)
        self.comboBox_metas.addItems(self.metas_name_list)
        self.cid = cid
        self.init_post_detail()
        self.show()
    

class Create_meta(QMainWindow, Ui_create_meta):
    def __init__(self, parent=None):
        super(Create_meta, self).__init__(parent)
        self.setupUi(self)

    def pass_value(self, metas_detail_list):
        self.metas_detail_list = metas_detail_list
        self.metas_detail_list[0]['name'] = '无父级分类'
        self.metas_name_list = [meta['name'] for meta in self.metas_detail_list]

    def open(self, metas_detail_list, row):
        self.pass_value(metas_detail_list)
        self.comboBox_metas.clear()
        self.comboBox_metas.addItems(self.metas_name_list)
        self.comboBox_metas.setCurrentIndex(-1) if row == 0 else self.comboBox_metas.setCurrentIndex(row)
        self.show()


class Update_meta(QMainWindow, Ui_update_meta):
    def __init__(self, parent=None):
        super(Update_meta, self).__init__(parent)
        self.setupUi(self)

    def pass_value(self, metas_detail_list):
        self.metas_detail_list = metas_detail_list
        self.metas_detail_list[0]['name'] = '无父级分类'
        self.metas_name_list = [meta['name'] for meta in self.metas_detail_list]

    def open(self, metas_detail_list, mid):
        self.pass_value(metas_detail_list)
        self.comboBox_metas.clear()
        self.comboBox_metas.addItems(self.metas_name_list)        
        self.mid = mid
        self.init_meta_detail()
        self.show()


class Create_page(QMainWindow, Ui_create_page):
    def __init__(self, parent=None):
        super(Create_page, self).__init__(parent)
        self.setupUi(self)


class Update_page(QMainWindow, Ui_update_page):
    def __init__(self, parent=None):
        super(Update_page, self).__init__(parent)
        self.setupUi(self)

    def open(self, cid):
        self.cid = cid
        self.init_page_detail()
        self.show()


class Settings(QMainWindow, Ui_settings):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        self.setupUi(self)


class Delete_meta(QMainWindow):
    list_update_metas_signal = pyqtSignal()
    list_update_passages_signal = pyqtSignal()
    def delete_meta(self, metas_detail_list, row):
        operation = Operation()
        if operation.delete_meta(metas_detail_list, row):
            QMessageBox.information(None, '删除分类', '删除分类成功', QMessageBox.Ok, QMessageBox.Ok)
            self.list_update_metas_signal.emit()
            self.list_update_passages_signal.emit()
        else:
            QMessageBox.warning(None, '删除分类', '删除分类失败！', QMessageBox.Ok, QMessageBox.Ok)


class Delete_passage(QMainWindow):
    list_update_passages_signal = pyqtSignal()
    def delete_post(self, cid):
        operation = Operation()
        if operation.delete_post(cid):
            QMessageBox.information(None, '删除文章', '删除文章成功', QMessageBox.Ok, QMessageBox.Ok)
            self.list_update_passages_signal.emit()
        else:
            QMessageBox.warning(None, '删除文章', '删除文章失败！', QMessageBox.Ok, QMessageBox.Ok)
    def delete_page(self, cid):
        operation = Operation()
        if operation.delete_page(cid):
            QMessageBox.information(None, '删除独立页面', '删除独立页面成功', QMessageBox.Ok, QMessageBox.Ok)
            self.list_update_passages_signal.emit()
        else:
            QMessageBox.warning(None, '删除独立页面', '删除独立页面失败！', QMessageBox.Ok, QMessageBox.Ok)


class Delete_post(QMainWindow):
    list_update_passages_signal = pyqtSignal()
    def delete_post(self, cid):
        operation = Operation()
        if operation.delete_post(cid):
            QMessageBox.information(None, '删除文章', '删除文章成功', QMessageBox.Ok, QMessageBox.Ok)
            self.list_update_passages_signal.emit()
        else:
            QMessageBox.warning(None, '删除文章', '删除文章失败！', QMessageBox.Ok, QMessageBox.Ok)


class Backups_all(QMainWindow, Ui_backups_all):
    def __init__(self, parent=None):
        super(Backups_all, self).__init__(parent)
        self.setupUi(self)
    def open(self):
        self.show() 
        self.start()


def main():

    app = QApplication(sys.argv)  

    #主窗口
    mainwindow = MainWindow()  
    mainwindow.show()


    #创建文章
    create_post = Create_post()
    mainwindow.pushButton_create_post.clicked.connect(
        lambda: create_post.open(mainwindow.metas_detail_list, mainwindow.listView_metas.currentIndex().row()))
    create_post.list_update_passages_signal.connect(
        lambda: create_post.pass_value(mainwindow.metas_detail_list))
    create_post.list_update_passages_signal.connect(
        lambda: mainwindow.list_posts(0) 
            if mainwindow.listView_metas.currentIndex().row() == -1 or mainwindow.listView_metas.currentIndex().row() == 0
            else mainwindow.list_posts(mainwindow.metas_detail_list[mainwindow.listView_metas.currentIndex().row()]['mid']))


    #更新文章
    update_post = Update_post()
    mainwindow.pushButton_update_post.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先进入分类文章界面！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.list_info != 'posts'
            else QMessageBox.warning(None, '提示', '请先选中要更新的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else update_post.open(mainwindow.metas_detail_list, mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid']))
    update_post.list_update_passages_signal.connect(
        lambda: update_post.pass_value(mainwindow.metas_detail_list))
    update_post.list_update_passages_signal.connect(
        lambda: mainwindow.list_posts(0) 
            if mainwindow.listView_metas.currentIndex().row() == -1 or mainwindow.listView_metas.currentIndex().row() == 0
            else mainwindow.list_posts(mainwindow.metas_detail_list[mainwindow.listView_metas.currentIndex().row()]['mid']))


    #快速更新文章
    mainwindow.pushButton_update_post_fast.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先进入分类文章界面！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.list_info != 'posts'
            else QMessageBox.warning(None, '提示', '请先选中要快速更新的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else update_post_fast())
    def update_post_fast():
        operation = Operation()
        return operation.update_post_fast(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid'])


    #创建独立页面
    create_page = Create_page()
    mainwindow.pushButton_create_page.clicked.connect(create_page.show)
    create_page.list_update_pages_signal.connect(mainwindow.list_pages)
    #create_page.list_update_pages_signal.connect(mainwindow.cancel_selected_meta)


    #更新独立页面
    update_page = Update_page()
    mainwindow.pushButton_update_page.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先进入独立页面界面！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.list_info != 'pages'
            else QMessageBox.warning(None, '提示', '请先选中要更新的独立页面！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else update_page.open(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid']))
    update_page.list_update_pages_signal.connect(mainwindow.list_pages)


    #快速更新独立页面
    mainwindow.pushButton_update_page_fast.clicked.connect(
        lambda:  QMessageBox.warning(None, '提示', '请先进入独立页面界面！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.list_info != 'pages'
            else QMessageBox.warning(None, '提示', '请先选中要快速更新的独立页面！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else update_page_fast())
    def update_page_fast():
        operation = Operation()
        return operation.update_page_fast(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid'])


    #创建分类
    create_meta = Create_meta()
    mainwindow.pushButton_create_meta.clicked.connect(lambda: create_meta.open(mainwindow.metas_detail_list, mainwindow.listView_metas.currentIndex().row()))
    create_meta.list_update_metas_signal.connect(lambda: create_meta.pass_value(mainwindow.metas_detail_list))
    create_meta.list_update_metas_signal.connect(mainwindow.list_metas)
    create_meta.comboBox_update_metas_signal.connect(lambda: create_meta.comboBox_update_metas(mainwindow.metas_detail_list))


    #更新分类
    update_meta = Update_meta()
    mainwindow.pushButton_update_meta.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要更新的分类！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_metas.currentIndex().row() == -1 
            else update_meta.open(mainwindow.metas_detail_list, mainwindow.metas_detail_list[mainwindow.listView_metas.currentIndex().row()]['mid']))
    update_meta.list_update_metas_signal.connect(lambda: update_meta.pass_value(mainwindow.metas_detail_list))
    update_meta.list_update_metas_signal.connect(mainwindow.list_metas)


    #删除分类
    delete_meta = Delete_meta()
    mainwindow.pushButton_delete_meta.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要删除的分类！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_metas.currentIndex().row() == -1 or mainwindow.listView_metas.currentIndex().row() == 0
            else delete_meta.delete_meta(mainwindow.metas_detail_list, mainwindow.listView_metas.currentIndex().row()))
    delete_meta.list_update_metas_signal.connect(mainwindow.list_metas)
    delete_meta.list_update_passages_signal.connect(lambda: mainwindow.list_posts(0))


    #下载文章
    mainwindow.pushButton_download.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要下载的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else download())
    def download():
        operation = Operation()
        return operation.download_passage(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid'])


    #下载并打开文章
    mainwindow.pushButton_download_and_open.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要打开的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else download_and_open_passage())
    def download_and_open_passage():
        operation = Operation()
        return operation.download_and_open_passage(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid'])


    #下载文章并下载其中图片
    mainwindow.pushButton_download_with_img.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要打开的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else download_passage_with_img(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid']))
    def download_passage_with_img(cid):
        operation = Operation()
        return operation.download_passage_with_img(cid)


    #打开文件
    mainwindow.pushButton_open_file.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要打开的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1 
            else open_file())
    def open_file():
        operation = Operation()
        return operation.open_file(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['title'])


    #打开缓存目录
    def open_dir():
        operation = Operation()
        return operation.open_dir()
    mainwindow.pushButton_open_dir.clicked.connect(open_dir)


    #删除文章
    delete_passage = Delete_passage()
    mainwindow.pushButton_delete_passage.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中要删除的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1
            else delete_passage.delete_post(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid'])
            if mainwindow.list_info == 'posts'
            else delete_passage.delete_page(mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid']))
    delete_passage.list_update_passages_signal.connect(
        lambda: mainwindow.list_pages()
            if mainwindow.list_info == 'pages'
            else mainwindow.list_posts(0)
            if mainwindow.listView_metas.currentIndex().row() == -1 or mainwindow.listView_metas.currentIndex().row() == 0
            else mainwindow.list_posts(mainwindow.metas_detail_list[mainwindow.listView_metas.currentIndex().row()]['mid']))


    #打开网页
    def open_url(type, slug):
        if type == 'posts':
            url = r'{}/index.php/archives/{}/'.format(mainwindow.operation.typecho.url, slug)
        else:
            url = r'{}/index.php/{}.html'.format(mainwindow.operation.typecho.url, slug)
        from webbrowser import open
        open(url)
    mainwindow.pushButton_open_url.clicked.connect(
        lambda: QMessageBox.warning(None, '提示', '请先选中打开网页的文章！', QMessageBox.Ok, QMessageBox.Ok)
            if mainwindow.listView_passages.currentIndex().row() == -1
            else open_url('posts', mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['cid'])
            if mainwindow.list_info == 'posts'
            else open_url('pages', mainwindow.passages_detail_list[mainwindow.listView_passages.currentIndex().row()]['slug']))
    

    #全站备份
    backups_all = Backups_all()
    mainwindow.pushButton_backups_all.clicked.connect(backups_all.open)


    #配置
    settings = Settings()
    mainwindow.pushButton_settings.clicked.connect(settings.show)
    settings.change_choose_blog_signal.connect(mainwindow.not_qt_creater)

    sys.exit(app.exec_())


if __name__=="__main__":  
    main()