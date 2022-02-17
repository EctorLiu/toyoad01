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
strJohnboToken = 'W9a3o7JtKinyfgBRf9oX3oFRIXvrcYKC5XC7yl5KCqV'
# 冠伶權杖：
strGwenToken = 'iEzx2cl5okBWmUb8f2BAD23esOvUKRNmwBIp7sIFpWU'
# 昆霖權杖：
strKunToken = '7MQCitn5m7DACt46wnpXJOFVhiwVdRAhBMpolK74rbG'
# 汶靜權杖：
strJingToken = 'L2e5pzTfF3a22jFIiZ1tQ2VN9lSrTDZ7A0nO3jzhwpL'
# 宜庭權杖：        
strMichelleToken = 'GksGM2RNtFn3TKz55ajI6ovsJgDcE7AmxJxvgk44Sey'
# 玉敏權杖：        
strMinToken = 'Z25DvEJjmkdubIEdjK4RUiIQvYiAtOvdG6HjdqHewWR'
# MOMO權杖：        
strMomoToken = 'fFmh2ao2ebztFgUT0VhOZDsGNN60CaxYtirCtkkl7Yj'
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


    ##### 選單資料 ######
GVstrSOPList01 = 'SOP清單：\n' + \
                                '（一）郵件\n' + \
                                '> (A) 台南大廳郵件領用SOP：\n' + \
                                ' (冠伶檔案修訂中)\n' + \
                                '\n' + \
                                '（二）餐廳電視 \n' + \
                                '> (A) 台南4F餐廳電視開啟SOP：\n' + \
                                '  連線：https://bit.ly/36e5kvn\n' + \
                                '\n' + \
                                '（三）宿舍\n' + \
                                '> (A) 台南長溪路宿舍保全設定SOP：\n' + \
                                '  連線：https://bit.ly/353NVVz'

#https://github.com/EctorLiu/toyoad01/raw/main/files/(New)SOP_TN4F_TV01.pptx
#https://github.com/EctorLiu/toyoad01/raw/main/files/(New)SOP_TNDorm01_Safety01.pdf
    # ***** ***** ***** ***** *****


    ##### 教學資料 ######
GVstrLineNotifyHowToGetToken = 'Line Notify推播說明：\n' + \
                                '「Line Notify」推播需要取得「權杖」，取得方式說明：\n' + \
                                '> 推播範例：\n' + \
                                '    畫面：https://bit.ly/3BmN9iR\n' + \
                                '\n' + \
                                ' Step01：進入網站並以自己帳號登入\n' + \
                                '> Line Notify網址：\n' + \
                                '         https://notify-bot.line.me/my/\n' + \
                                '> 圖片說明：\n' + \
                                '    畫面：https://bit.ly/3gN7oMT\n' + \
                                '\n' + \
                                'Step02：之後進入右上角的「個人頁面」\n' + \
                                '> 圖片說明：\n' + \
                                '    畫面：https://bit.ly/3rQTUGi\n' + \
                                '\n' + \
                                'Step03：點選下方「發行權杖」按鈕\n' + \
                                '> 圖片說明：\n' + \
                                '    畫面：https://bit.ly/3JtpHDe\n' + \
                                '\n' + \
                                'Step04：設定推播時的名稱\n' + \
                                '  4-1. 填寫權杖名稱\n' + \
                                '  4-2. 點選「透過1對1聊天接收LINE Notify的通知」\n' + \
                                '  4-3. 點選「發行」\n' + \
                                '> 圖片說明：\n' + \
                                '    畫面：https://bit.ly/3oRVSoe\n' + \
                                '\n' + \
                                'Step05：取得權杖（文字字串）\n' + \
                                '> 可以點選複製按鈕，提供該字串資料即可\n' + \
                                '> 圖片說明：\n' + \
                                '    畫面：https://bit.ly/3GSCg9q\n' + \
                                '\n' + \
                                '\n' + \
                                '其他補充：若上述完成後仍無法LineNotify推播：\n' + \
                                '> (1) 可手動加入LineNotify服務\n' + \
                                '>   ID搜尋：「@linenotify」\n' + \
                                '    畫面：https://bit.ly/33qAr5W\n' + \
                                '> (2) 可確認Line設定是否有「阻擋訊息」\n' + \
                                '    畫面：https://bit.ly/3HVA2Yc\n' + \
                                ''
    # ***** ***** ***** ***** *****


    ##### 關鍵字清單 ######
GVstrCMKeyWord = 'KW：\n' + \
                '[開放使用]\n' + \
                '(1)(SOP) + (清單 or 下載)\n' + \
                '\n' + \
                '[推播功能]\n' + \
                '(TY or TOYO) + \n' + \
                '(1)推播ECTOR + 內容\n' + \
                '(2)推播智弘 + 內容\n' + \
                '(3)推播冠伶 + 內容\n' + \
                '(4)推播昆霖 + 內容\n' + \
                '(5)推播汶靜 + 內容\n' + \
                '(6)推播宜庭 + 內容\n' + \
                '(7)推播玉敏 + 內容\n' + \
                '(8)推播MOMO + 內容\n' + \
                '(9)推播全部 + 內容\n' + \
                '\n' + \
                '[關鍵字]\n' + \
                '(1)如何使用/HELP/?/？\n' + \
                '(2)(最近 or 最新) + (訊息 or 活動)\n' + \
                '\n' + \
                '[資料庫]\n' + \
                '(1)宿舍防疫 + (房間 or 人名)\n' + \
                '(2)面試報到\n' + \
                '(3)業務電話\n' + \
                '(4)夜點晚餐\n' + \
                '(5)防疫群組\n' + \
                '(6)體溫回報\n' + \
                '(7)車輛查詢 + (車牌 or 人名)\n' + \
                '\n' + \
                '[內部使用]\n' + \
                '(1)(TY or TOYO) + (DOOR or 門禁)\n' + \
                '(2)(TY or TOYO) + (NEWFE or 新滅火)\n' + \
                '(3)(TY or TOYO) + (FE or 滅火)\n' + \
                '\n' + \
                '[教學]\n' + \
                '(1)(TY or TOYO) + (推播權杖教學)\n' + \
                '(2)(TY or TOYO) + (官方帳號教學)'
    # ***** ***** ***** ***** *****


    ##### 關鍵字清單 ######
GVstrECKeyWord = 'KW：\n' + \
                '[開放使用]\n' + \
                '(1)(SOP) + (清單 or 下載)\n' + \
                '\n' + \
                '[推播功能]\n' + \
                '(TY or TOYO) + \n' + \
                '(1)推播PROG + 內容\n' + \
                '(2)推播ECTOR + 內容\n' + \
                '(3)推播智弘 + 內容\n' + \
                '(4)推播冠伶 + 內容\n' + \
                '(5)推播昆霖 + 內容\n' + \
                '(6)推播宜庭 + 內容\n' + \
                '(7)推播玉敏 + 內容\n' + \
                '(8)推播MOMO + 內容\n' + \
                '(9)推播全部 + 內容\n' + \
                '\n' + \
                '[關鍵字]\n' + \
                '(1)如何使用/HELP/?/？\n' + \
                '(2)(最近 or 最新) + (訊息 or 活動)\n' + \
                '\n' + \
                '[資料庫]\n' + \
                '(1)宿舍防疫 + (房間 or 人名)\n' + \
                '(2)面試報到\n' + \
                '(3)業務電話\n' + \
                '(4)夜點晚餐\n' + \
                '(5)防疫群組\n' + \
                '(6)體溫回報\n' + \
                '(7)車輛查詢 + (車牌 or 人名)\n' + \
                '\n' + \
                '[內部使用]\n' + \
                '(1)(TY or TOYO) + (DOOR or 門禁)\n' + \
                '(2)(TY or TOYO) + (NEWFE or 新滅火)\n' + \
                '(3)(TY or TOYO) + (FE or 滅火)\n' + \
                '\n' + \
                '[教學]\n' + \
                '(1)(TY or TOYO) + (推播權杖教學)\n' + \
                '(2)(TY or TOYO) + (官方帳號教學)\n' + \
                '\n' + \
                '[測試中]\n' + \
                'TSVI +\n' + \
                '(1)樣版\n' + \
                '\n' + \
                '[ECTOR]\n' + \
                '(1)(TY or TOYO) + (MEMO)\n' + \
                '(2)(TY or TOYO) + (120 or $ or MONEY or 零用金)\n' + \
                '\n(A)E.4. + HN + (KW or LINE)'
    # ***** ***** ***** ***** *****

