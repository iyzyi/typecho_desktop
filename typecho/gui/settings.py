# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from typecho.logic.operation import Operation
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal

class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(358, 275)
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 206))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_blog = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_blog.setObjectName("comboBox_blog")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_blog)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_blog_url = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_blog_url.setObjectName("lineEdit_blog_url")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_blog_url)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_blog_token1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_blog_token1.setObjectName("lineEdit_blog_token1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_blog_token1)
        self.lineEdit_database_ip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_database_ip.setObjectName("lineEdit_database_ip")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_database_ip)
        self.lineEdit_database_user = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_database_user.setObjectName("lineEdit_database_user")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_database_user)
        self.lineEdit_database_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_database_name.setObjectName("lineEdit_database_name")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_database_name)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_database_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_database_password.setObjectName("lineEdit_database_password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_database_password)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_localDir = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_localDir.setObjectName("lineEdit_localDir")
        self.horizontalLayout_2.addWidget(self.lineEdit_localDir)
        self.toolButton = QtWidgets.QToolButton(self.formLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 341, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add_blog = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_add_blog.setObjectName("pushButton_add_blog")
        self.horizontalLayout.addWidget(self.pushButton_add_blog)
        self.pushButton_update_blog = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_update_blog.setObjectName("pushButton_update_blog")
        self.horizontalLayout.addWidget(self.pushButton_update_blog)
        self.pushButton_choose_blog = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_choose_blog.setObjectName("pushButton_choose_blog")
        self.horizontalLayout.addWidget(self.pushButton_choose_blog)
        settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 23))
        self.menubar.setObjectName("menubar")
        settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settings)
        self.statusbar.setObjectName("statusbar")
        settings.setStatusBar(self.statusbar)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)
        self.not_qt_creater()


    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "客户端配置"))
        self.label.setText(_translate("settings", "选择博客"))
        self.label_2.setText(_translate("settings", "博客URL"))
        self.label_3.setText(_translate("settings", "博客token1"))
        self.label_4.setText(_translate("settings", "数据库IP"))
        self.label_5.setText(_translate("settings", "数据库用户名"))
        self.label_6.setText(_translate("settings", "数据库库名"))
        self.label_7.setText(_translate("settings", "本地缓存路径"))
        self.label_8.setText(_translate("settings", "数据库密码"))
        self.toolButton.setText(_translate("settings", "..."))
        self.pushButton_add_blog.setText(_translate("settings", "添加博客"))
        self.pushButton_update_blog.setText(_translate("settings", "修改信息"))
        self.pushButton_choose_blog.setText(_translate("settings", "选择此博客"))


    change_choose_blog_signal = pyqtSignal()
    

    def not_qt_creater(self):
        operation = Operation()
        if operation.exists_settings():
            self.show_func = lambda: self.init_blog_detail(self.comboBox_blog.currentIndex())
            self.comboBox_blog.currentIndexChanged.connect(self.show_func)
            
            choose_blog_num, self.blogs_detail_list = operation.get_settings_info()
            choose_blog = self.blogs_detail_list[choose_blog_num]
            self.init_blog_detail(choose_blog_num)         

            self.pushButton_add_blog.clicked.connect(self.add_blog_setting)
            self.pushButton_update_blog.clicked.connect(self.update_blog_setting)
            self.pushButton_choose_blog.clicked.connect(self.choose_blog_setting)
            self.toolButton.clicked.connect(self.get_dir)  

    
    def get_dir(self):
        operation = Operation()
        localDir = operation.typecho.localDir
        dir = QtWidgets.QFileDialog.getExistingDirectory(None, '选择要创建的文章', localDir)
        self.lineEdit_localDir.setText(dir.replace('/','\\'))   #不转化的话莫名其妙地打开缓存目录失败


    def init_blog_detail(self, show_blog_num):
        choose_blog = self.blogs_detail_list[show_blog_num]
        blogs_url_list = [blog['url'] for blog in self.blogs_detail_list]

        self.comboBox_blog.currentIndexChanged.disconnect(self.show_func)
        self.comboBox_blog.clear()
        self.comboBox_blog.addItems(blogs_url_list)
        self.comboBox_blog.setCurrentIndex(show_blog_num)
        self.comboBox_blog.currentIndexChanged.connect(self.show_func)

        self.lineEdit_blog_url.setText(choose_blog['url'])
        self.lineEdit_blog_token1.setText(choose_blog['token1'])
        self.lineEdit_database_ip.setText(choose_blog['ip'])
        self.lineEdit_database_user.setText(choose_blog['user'])
        self.lineEdit_database_password.setText(choose_blog['password'])
        self.lineEdit_database_name.setText(choose_blog['database'])
        self.lineEdit_localDir.setText(choose_blog['localDir'])


    def get_current_blog_info(self):
        choose_blog = {
            'url': self.lineEdit_blog_url.text(),
            'token1': self.lineEdit_blog_token1.text(),
            'ip': self.lineEdit_database_ip.text(),
            'user': self.lineEdit_database_user.text(),
            'password': self.lineEdit_database_password.text(),
            'database': self.lineEdit_database_name.text(),
            'localDir': self.lineEdit_localDir.text()
        }
        return choose_blog
    

    def check_exists(self):
        choose_blog = self.get_current_blog_info()
        operation = Operation()
        for blog in self.blogs_detail_list:
            try:
                del blog['num']
            except:
                pass
            if blog == choose_blog:
                return True
        return False


    def add_blog_setting(self):
        if not self.check_exists():
            choose_blog = self.get_current_blog_info()
            operation = Operation()
            operation.add_blog_setting(choose_blog)

            choose_blog_num, self.blogs_detail_list = operation.get_settings_info()
            choose_blog = self.blogs_detail_list[choose_blog_num]
            self.init_blog_detail(choose_blog_num) 

            operation = Operation()
            choose_blog_num, self.blogs_detail_list = operation.get_settings_info()
            QMessageBox.information(None, '添加博客配置', '添加成功', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '添加博客', '博客配置信息已存在！', QMessageBox.Ok, QMessageBox.Ok)


    def update_blog_setting(self):
        choose_blog = self.get_current_blog_info()
        operation = Operation()
        operation.update_blog_setting(self.comboBox_blog.currentIndex(), choose_blog)
        #print(self.comboBox_blog.currentIndex())

        choose_blog_num, self.blogs_detail_list = operation.get_settings_info()
        choose_blog = self.blogs_detail_list[choose_blog_num]
        self.init_blog_detail(choose_blog_num)
        QMessageBox.information(None, '更新博客配置', '更新成功', QMessageBox.Ok, QMessageBox.Ok)


    def choose_blog_setting(self):
        operation = Operation()
        operation.choose_blog_setting(self.comboBox_blog.currentIndex())
        self.change_choose_blog_signal.emit()