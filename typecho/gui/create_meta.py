# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_meta.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from typecho.logic.operation import Operation

class Ui_create_meta(object):
    def setupUi(self, create_meta):
        create_meta.setObjectName("create_meta")
        create_meta.resize(430, 264)
        self.centralwidget = QtWidgets.QWidget(create_meta)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_slug = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_slug.setObjectName("lineEdit_slug")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_slug)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_metas = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_metas.setObjectName("comboBox_metas")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_metas)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit_description = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_description.setObjectName("textEdit_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_description)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        create_meta.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(create_meta)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 23))
        self.menubar.setObjectName("menubar")
        create_meta.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(create_meta)
        self.statusbar.setObjectName("statusbar")
        create_meta.setStatusBar(self.statusbar)

        self.retranslateUi(create_meta)
        QtCore.QMetaObject.connectSlotsByName(create_meta)
        self.not_qt_designer()

    def retranslateUi(self, create_meta):
        _translate = QtCore.QCoreApplication.translate
        create_meta.setWindowTitle(_translate("create_meta", "创建分类"))
        self.label.setText(_translate("create_meta", "分类名称"))
        self.label_2.setText(_translate("create_meta", "分类缩略名"))
        self.label_3.setText(_translate("create_meta", "父级分类"))
        self.label_4.setText(_translate("create_meta", "分类描述"))
        self.pushButton.setText(_translate("create_meta", "创建分类"))

    
    list_update_metas_signal = QtCore.pyqtSignal()
    comboBox_update_metas_signal = QtCore.pyqtSignal()


    def not_qt_designer(self):
        self.pushButton.clicked.connect(self.start)


    def start(self):
        name = self.lineEdit_name.text()
        slug = self.lineEdit_slug.text()
        row = self.comboBox_metas.currentIndex()
        parent =  0 if row == -1 or row == 0 else self.metas_detail_list[self.comboBox_metas.currentIndex()]['mid']
        description = self.textEdit_description.toPlainText()
        try:
            operation = Operation()
            r = operation.create_meta(name, slug, parent, description)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, '创建分类', '程序运行错误！\n%s'%str(e), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            dict = {
                '-1':   '分类名称已经存在',
                '-2':   '缩略名已经存在',
                '-3':   '分类名称和缩略名都已存在',
                '-4':   '未知错误'
            }
            if r < 0:
                QtWidgets.QMessageBox.warning(self, '创建分类', dict[str(r)], QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            else:
                reply = QtWidgets.QMessageBox.information(None, '创建分类', '创建分类成功！\n分类：%s, mid：%d\n是否继续创建分类？' % (name, r), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
                self.Ui_clear()
                self.list_update_metas_signal.emit()
                if reply == QtWidgets.QMessageBox.No:
                    self.close()
                else:
                    self.comboBox_update_metas_signal.emit()    #先更新列表，再更新下拉菜单（因为下拉菜单的值从列表中获取）

        
        
    def comboBox_update_metas(self, metas_detail_list):
        self.metas_detail_list = metas_detail_list
        self.metas_detail_list[0]['name'] = '无父级分类'
        self.metas_name_list = [meta['name'] for meta in self.metas_detail_list]
        self.comboBox_metas.clear()
        self.comboBox_metas.addItems(self.metas_name_list)

        
    def Ui_clear(self):
        self.lineEdit_name.setText('')
        self.lineEdit_slug.setText('')
        self.comboBox_metas.setCurrentIndex(-1)
        self.textEdit_description.setText('') 