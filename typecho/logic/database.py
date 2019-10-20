import pymysql
from PyQt5.QtWidgets import QMessageBox

class DB():

    def __init__(self, ip, user, password, database):
        self.ip = ip
        self.user = user
        self.password = password
        self.database = database
        #self.print_sql = print_sql
        try:
            self.db = pymysql.connect(ip, user, password, database)
        except Exception as e:
            QMessageBox.information(None, '数据库', '数据库连接失败！\n%s' % str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.cursor = self.db.cursor()
            self.cursor.execute('SELECT uid,authCode FROM typecho_users')
            user_info = self.cursor.fetchone()
            self.user_uid = user_info[0]
            self.user_authCode = user_info[1]