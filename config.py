# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====
import os

# ===== ===== ===== ===== ===== 【變數區域】 ===== ===== ===== ===== =====

    ##### Line ######
# line-bot
strchannel_access_token = os.environ.get("CHANNEL_ACCESS_TOKEN")
strchannel_secret = os.environ.get("CHANNEL_SECRET")

# channel_access_token = 'CHANNEL_ACCESS_TOKEN' 
# channel_secret = 'CHANNEL_SECRET'
    # ***** ***** ***** ***** *****


    ##### 權杖資料 ######
    # strEctorToken、strJohnboToken、strGwenToken、strKunToken、strMichelleToken
# EctorLiu權杖：
strEctorToken = 'rOvcCpmikeueH0xYaSLacH8ya3kBDCJPeySEWyjb6KC'
# 智弘權杖：
strJohnboToken = ''
# 冠伶權杖：
strGwenToken = ''
# 昆霖權杖：
strKunToken = ''
# 宜庭權杖：        
strMichelleToken = ''
    # ***** ***** ***** ***** *****


    ##### SQL ######
import pymssql

GVstr254_host = '211.23.242.222'
GVstr254_port = '2255'
GVstr254_user = 'sa'
GVstr254_pwd = '00000'
GVstr254_TIM_DB = 'TIM_DB'

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
        # strSQLCond = "RS_SQL_ExecQuery OK"
        # return strSQLCond

    def RS_SQL_ExecNonQuery(self, sql):
        cur = self.RS_SQL_GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

# sql語句中有中文的時候進行encode
# insertSql = "insert into WeiBo([UserId],[WeiBoContent],[PublishDate]) values(1,'測試','2012/2/1')".encode("utf8")
# 連線的時候加入charset設定資訊
# pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')

# conn = pymssql.connect(host='192.168.1.254', user='sa', password='00000')
# conn = pymssql.connect(host='192.168.1.254', port=1433, user='sa',password='00000',database='TIM_DB',charset='utf8', as_dict=True)
# conn = pymssql.connect('192.168.1.254','sa', '00000', 'TIM_DB')
# conn = pymssql.connect('211.23.242.220','sa@211.23.242.220', 'Sql#dsc20170524', 'TIMHRDB')
# cursor = conn.cursor(as_dict=True)
    # ***** ***** ***** ***** *****


    ##### 關鍵字清單 ######
GVstrKeyWord = '參考內容：' + \
                '    if temp_message == '您好':\n' + \
                '\n' + \
                '    # ***** ***** ***** ***** *****\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播PROG' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播ECTOR' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播智弘' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播冠伶' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播昆霖' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播宜庭' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('推播全部' in temp_message.upper()):\n' + \
                '    # ***** ***** ***** ***** *****\n' + \
                '    \n' + \
                '    ##### TSVI樣版 #####\n' + \
                '    elif (temp_message[0:4].upper() == 'TSVI') and \\n' + \
                '            ('樣版' in temp_message.upper()):\n' + \
                '        get_TYPE_message = 'TSVI樣版'   \n' + \
                '    # ***** ***** ***** ***** *****\n' + \
                '\n' + \
                '\n' + \
                '    ##### 關鍵字 #####\n' + \
                '    elif ('如何使用' in temp_message or 'HELP' in temp_message.upper() or '?' in temp_message.strip() or '？' in temp_message.strip()):\n' + \
                '    elif ('最近' in temp_message or '最新' in temp_message) and ('訊息' in temp_message or '活動' in temp_message):\n' + \
                '    elif ('宿舍防疫' in temp_message.upper()):\n' + \
                '    elif ('面試報到' in temp_message.upper()):（可加參數）\n' + \
                '    elif ('業務電話' in temp_message.upper()):\n' + \
                '    elif ('夜點晚餐' in temp_message.upper()):\n' + \
                '    elif ('防疫群組' in temp_message.upper()):\n' + \
                '    elif ('體溫回報' in temp_message.upper()):\n' + \
                '\n' + \
                '    # ***** ***** ***** ***** *****\n' + \
                '    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \\n' + \
                '            ('120' in temp_message.upper() or \\n' + \
                '            '$' in temp_message.upper() or \\n' + \
                '            'MONEY' in temp_message.upper() or \\n' + \
                '            '零用金' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \\n' + \
                '            ('DOOR' in temp_message.upper() or \\n' + \
                '            '門禁' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \\n' + \
                '            ('NEWFE' in temp_message.upper() or \\n' + \
                '            '新滅火' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \\n' + \
                '            ('FE' in temp_message.upper() or \\n' + \
                '            '滅火' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \\n' + \
                '            ('MEMO' in temp_message.upper()):\n' + \
                '    elif (temp_message[0:5].upper() == 'ECTOR') and ('官方帳號教學' in temp_message):\n' + \
                '    # ***** ***** ***** ***** *****\n' + \
                '\n' + \
                '    ##### (Ver)版本 #####\n' + \
                '    elif temp_message.upper().count('VER') > 0:\n' + \
                '    # ***** ***** ***** ***** *****'

