# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backups_all.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from typecho.logic.operation import Operation

class Ui_backups_all(object):
    def setupUi(self, backups_all):
        backups_all.setObjectName("backups_all")
        backups_all.resize(392, 114)
        self.centralwidget = QtWidgets.QWidget(backups_all)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 371, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 20))
        self.label.setObjectName("label")
        backups_all.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(backups_all)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 23))
        self.menubar.setObjectName("menubar")
        backups_all.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(backups_all)
        self.statusbar.setObjectName("statusbar")
        backups_all.setStatusBar(self.statusbar)

        self.retranslateUi(backups_all)
        QtCore.QMetaObject.connectSlotsByName(backups_all)

    def retranslateUi(self, backups_all):
        _translate = QtCore.QCoreApplication.translate
        backups_all.setWindowTitle(_translate("backups_all", "全站备份"))
        self.label.setText(_translate("backups_all", "正在下载"))

    def start(self):
        operation = Operation()
        passages = operation.get_all_cids_with_title()
        self.count = len(passages)
        self.success = self.fail = 0
        for passage in passages:
            try:
                self.label.setText('正在下载：%s' % passage['title'])
                operation.typecho.download_passage_with_img(passage['cid'])
            except Exception as e:
                #print(e)
                self.fail += 1
            else:
                self.success += 1
                self.progressBar.setProperty("value", (self.success+self.fail)//self.count)
        QtWidgets.QMessageBox.information(None, '全站备份', '备份完成！\n成功：%d\n失败：%d' %(self.success, self.fail), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
