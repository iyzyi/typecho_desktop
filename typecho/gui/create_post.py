# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_post.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from typecho.logic.operation import Operation
import os.path

class Ui_create_post(object):
    def setupUi(self, create_post):
        create_post.setObjectName("create_post")
        create_post.resize(541, 294)
        self.centralwidget = QtWidgets.QWidget(create_post)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 233))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_title = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_title)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_img_url = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_img_url.setObjectName("lineEdit_img_url")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_img_url)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textEdit_preview = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_preview.setObjectName("textEdit_preview")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_preview)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_filepath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.horizontalLayout.addWidget(self.lineEdit_filepath)
        self.toolButton = QtWidgets.QToolButton(self.formLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.comboBox_metas = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_metas.setObjectName("comboBox_metas")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_metas)
        self.lineEdit_time = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_time)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        create_post.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(create_post)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 23))
        self.menubar.setObjectName("menubar")
        create_post.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(create_post)
        self.statusbar.setObjectName("statusbar")
        create_post.setStatusBar(self.statusbar)

        self.retranslateUi(create_post)
        QtCore.QMetaObject.connectSlotsByName(create_post)

        self.not_qt_desinger()


    def retranslateUi(self, create_post):
        _translate = QtCore.QCoreApplication.translate
        create_post.setWindowTitle(_translate("create_post", "创建文章"))
        self.label_6.setText(_translate("create_post", "标题"))
        self.label_5.setText(_translate("create_post", "分类"))
        self.label_4.setText(_translate("create_post", "创建时间"))
        self.label.setText(_translate("create_post", "缩略图Url"))
        self.label_2.setText(_translate("create_post", "文章预览内容"))
        self.label_3.setText(_translate("create_post", "文章目录"))
        self.toolButton.setText(_translate("create_post", "..."))
        self.label_7.setText(_translate("create_post", "文件路径"))
        self.checkBox.setText(_translate("create_post", "开启"))
        self.pushButton.setText(_translate("create_post", "开始上传"))

    
    list_update_passages_signal = QtCore.pyqtSignal()


    def not_qt_desinger(self):
        #self.checkBox.setChecked(True)
        self.toolButton.clicked.connect(self.getfile)
        self.lineEdit_time.setInputMask('0000-00-00 00:00;_')
        self.pushButton.clicked.connect(self.start)


    def getfile(self):
        operation = Operation()
        localDir = operation.typecho.localDir
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(None, '选择要创建的文章', localDir,"markdown files (*.md)")
        self.lineEdit_filepath.setText(filepath)
        import re, os
        self.lineEdit_title.setText(re.sub(r'\.md$', '', os.path.split(filepath)[1]))


    def start(self):
        filepath = self.lineEdit_filepath.text()
        title = self.lineEdit_title.text()
        row = self.comboBox_metas.currentIndex()
        meta = '' if row == -1 or row == 0 else self.metas_detail_list[self.comboBox_metas.currentIndex()]['mid']
        date = self.lineEdit_time.text() if self.lineEdit_time.text() != '-- :' else ''
        img_url = self.lineEdit_img_url.text()
        preview = self.textEdit_preview.toPlainText()
        h2h3 = '1' if self.checkBox.isChecked() else ''
        if filepath == '' or title == '':
            QtWidgets.QMessageBox.warning(self, '创建文章', '文件路径、标题为必填项', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        elif not os.path.exists(filepath):
            QtWidgets.QMessageBox.warning(self, '创建文章', '文件路径错误，文件不存在！', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            try:
                operation = Operation()
                r = operation.write_post(filepath, title, meta, date, img_url, preview, h2h3)
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, '创建文章', '程序运行错误！\n%s'%str(e), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            else:
                if not r:
                    QtWidgets.QMessageBox.warning(self, '创建文章', '创建文章失败！', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
                else:
                    reply = QtWidgets.QMessageBox.information(self, '创建文章', '创建文章成功！\n是否继续创建文章？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                    if reply == QtWidgets.QMessageBox.No:
                        self.close()
                    self.Ui_clear()
                    self.list_update_passages_signal.emit()


    def Ui_clear(self):     #清除创建文章窗口内的所有数据
        self.lineEdit_filepath.setText('')
        self.lineEdit_title.setText('')
        self.comboBox_metas.setCurrentIndex(-1)
        self.lineEdit_time.setText('')
        self.lineEdit_img_url.setText('')
        self.textEdit_preview.setText('')
        self.checkBox.setChecked(True)


'''
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_create_post()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
'''