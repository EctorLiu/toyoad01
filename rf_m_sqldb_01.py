    ##### INDEX ######
# def RS_SQL_GetConnect(self): 取得與資料庫的連線
# def RS_SQL_ExecQuery(self, sql): 查詢語法(Select)
# def RS_SQL_ExecNonQuery(self, sql): 非查詢語法(Update, Delete, Insert Into)
    # ***** ***** ***** ***** *****

    ##### 匯入函式庫 ######
import pymssql
    # ***** ***** ***** ***** *****

    ##### Initial ######
GVstr254_host = '211.23.242.222'
GVstr254_port = '2255'
GVstr254_user = 'sa'
GVstr254_pwd = '00000'
GVstr254_TIM_DB = 'TIM_DB'
    # ***** ***** ***** ***** *****


    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######

class MSSQL:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

    def RS_SQL_GetConnect(self):
        if not self.db:
            raise(NameError,"沒有設定資料庫資訊")
        self.conn = pymssql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"連線資料庫失敗")
            # strSQLCond = "Connect NG"
            # return strSQLCond
        else:
            return cur
            # strSQLCond = "Connect OK"
            # return strSQLCond

    def RS_SQL_ExecQuery(self, sql):
        cur = self.RS_SQL_GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def RS_SQL_ExecNonQuery(self, sql):
        cur = self.RS_SQL_GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    # ***** ***** ***** ***** *****

    ##### 備註區域 ######
# sql語句中有中文的時候進行encode
# insertSql = "insert into WeiBo([UserId],[WeiBoContent],[PublishDate]) values(1,'測試','2012/2/1')".encode("utf8")
# 連線的時候加入charset設定資訊
# pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
    # ***** ***** ***** ***** *****
