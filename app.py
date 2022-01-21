# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====

    ##### 版本 ######
strVer = '(M121)1225'

    # 切換SQL功能選擇：ON/OFF
strSQL_FW_Switch = 'ON'
    # 切換同仁推播功能選擇：ON/OFF
strPush_NotKeyWord2All_Switch = 'ON'
    # ***** ***** ***** ***** *****

    ##### 預設留言 ######
strNewestActivity = '『TOYO行政管理部』：最近活動\n' + \
                '更新：2022/01/17 17:20 ...\n\n' + \
                '..'

strMoneyText = '公費使用狀況'

strMemo = '公司住址：70947台南市安南區新吉三路55號\n' + \
            '導航：https://g.page/TOYOROBOT?share'

strHowToUse = '『TOYO行政管理部』：\n' + \
                'Hi！這是行政管理部之官方帳號！\n謝謝你的訊息！\n\n' + \
                '也許您可用下述常用關鍵字查詢：\n' + \
                '「面試報到」\n' + \
                '「業務電話」\n' + \
                '「夜點晚餐」\n' + \
                '「防疫群組」\n' + \
                '「體溫回報」\n' + \
                '「如何使用」\n' + \
                '「最新訊息」等..'

strLessonLearning = 'A1. 申請官方帳號：\n' + \
                    'https://manager.line.biz/\n' + \
                    '\n' + \
                    'A2. 自動回覆的類別有三種..\n' + \
                    '    (1) 『關鍵字』回應\n' + \
                    '    (2) 『智慧聊天』回應\n' + \
                    '    (3) 『程式』回應 (需自己寫程式)\n' + \
                    'A3. 第一種..『關鍵字』回應\n' + \
                    '    回應模式：選「聊天機器人」、Webhook：選「停用」\n' + \
                    'A4. 第二種..『智慧聊天』回應\n' + \
                    '    回應模式：選「聊天」\n' + \
                    'A5. 第三種..『程式』回應 (需自己寫程式)\n' + \
                    '    回應模式：選「聊天機器人」、Webhook：選「啟用」\n' + \
                    '    > 是用上面的設定決定哪一種回應方式..\n' + \
                    '\n' + \
                    'A6. 應用面的教學\n' + \
                    '    可參考範例1..\n' + \
                    'https://ithelp.ithome.com.tw/articles/10192259\n' + \
                    '    可參考範例2..\n' + \
                    'https://ithelp.ithome.com.tw/articles/10233234\n' + \
                    '\n' + \
                    'A7. 這個是我一開始看的官方文件：\n' + \
                    'https://developers.line.biz/zh-hant/docs/messaging-api/building-bot/\n' + \
                    'A8. 同上..Line官方有提供範例\n' + \
                    'https://developers.line.biz/zh-hant/docs/messaging-api/building-bot/\n' + \
                    '選擇語言進行開發..\n' + \
                    '\n' + \
                    'A9. 開發環境網站Line Develop（之後再看其他教學網站）\n' + \
                    'https://developers.line.biz/zh-hant/\n' + \
                    '\n' + \
                    'B1. 『推播』的話要拿權杖：\n' + \
                    'https://notify-bot.line.me/my/\n' + \
                    'B2. 『推播』教學可參考這一篇：\n' + \
                    'https://bustlec.github.io/note/2018/07/10/line-notify-using-python/'


    # ***** ***** ***** ***** *****

    ##### (TSVI)推播 ######
import requests
    # ***** ***** ***** ***** *****

    ##### 時間函數 ######
from datetime import datetime
import time
datNow = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) 
    # ***** ***** ***** ***** *****

    ##### Line ######
from config import * 
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

line_bot_api = LineBotApi(strchannel_access_token)
handler = WebhookHandler(strchannel_secret)
    # ***** ***** ***** ***** *****

    ##### Flask ######
from flask import Flask, abort, request
app = Flask(__name__)
    # ***** ***** ***** ***** *****

    ##### 日期時間 ######
from datetime import datetime
    # ***** ***** ***** ***** *****


# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====

@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 取得事件變數
    temp_message = event.message.text

    ##### 全型符號轉換 #####
    temp_message = temp_message.replace('！','!')
    temp_message = temp_message.replace('（','(')
    temp_message = temp_message.replace('）',')')
    temp_message = temp_message.replace('，',',')
    temp_message = temp_message.replace('＄','$')
    temp_message = temp_message.replace('？','?')
    # ***** ***** ***** ***** *****

    # 確認資料類別
    get_TYPE_message = 'Initial'

    if temp_message == '您好':
        # (A)禮貌回覆
        get_message = '『TOYO行政管理部』：您好' + event.message.text

    ##### (TSVI)推播 #####
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播PROG' in temp_message.upper()):
        get_TYPE_message = 'TSVI推播程式管理員'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播PROG', '')
        get_message = '(Admin)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播ECTOR' in temp_message.upper()):
        get_TYPE_message = 'TSVI2Ector'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播ECTOR', '')
        get_message = '(只推Ector)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播智弘' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2智弘'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播智弘', '')
        get_message = '(只推智弘)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播冠伶' in temp_message.upper()):
        get_TYPE_message = 'TSVI2冠伶'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播冠伶', '')
        get_message = '(只推冠伶)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播昆霖' in temp_message.upper()):
        get_TYPE_message = 'TSVI2昆霖'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播昆霖', '')
        get_message = '(只推昆霖)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播宜庭' in temp_message.upper()):
        get_TYPE_message = 'TSVI2宜庭'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播宜庭', '')
        get_message = '(只推宜庭)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播全部' in temp_message.upper()):
        get_TYPE_message = 'TSVI推播全部'
        temp_message = temp_message.replace('TSVI推播全部', '')
        get_message = '(推全部)\n' + temp_message
    # ***** ***** ***** ***** *****

    
    ##### TSVI樣版 #####
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('樣版' in temp_message.upper()):
        get_TYPE_message = 'TSVI樣版'   
    # ***** ***** ***** ***** *****


    ##### 關鍵字 #####
    elif ('如何使用' in temp_message or 'HELP' in temp_message.upper() or '?' in temp_message.strip() or '？' in temp_message.strip()):
        get_TYPE_message = 'How_To_Use'
        get_message = strHowToUse
    elif ('最近' in temp_message or '最新' in temp_message) and ('訊息' in temp_message or '活動' in temp_message):
        get_TYPE_message = 'New_Activity'
        get_message = strNewestActivity

    elif ('面試報到' in temp_message.upper()):
        strTitle = 'TOYO面試報到10天內'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            strSQL = 'SELECT AF_DAY, IN_TYPE, IN_DAY,IN_TIME,DEPT_CODE, IN_NAME ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_APP_MEM_IN_10_DAY] ' + \
                        ' ORDER BY [IN_DAY], [IN_TIME]'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (AF_DAY, IN_TYPE, IN_DAY, IN_TIME, DEPT_CODE, IN_NAME) in resList:
                intCount += 1
                if AF_DAY == '當天':
                    strTemp += '[' + str(intCount) + ']' + str(AF_DAY) + '..' + str(IN_TYPE) + ', ' + str(IN_DAY) + '\n' + \
                                '  ' + str(IN_TIME) + ', ' + str(DEPT_CODE) + ', ' + str(IN_NAME) + '\n\n'
                else:
                    strTemp += '[' + str(intCount) + ']還有' + str(AF_DAY) + '天..' + str(IN_TYPE) + ', ' + str(IN_DAY) + '\n' + \
                                '  ' + str(IN_TIME) + ', ' + str(DEPT_CODE) + ', ' + str(IN_NAME) + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('業務電話' in temp_message.upper()):
        strTitle = 'TOYO業務電話'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            strSQL = 'SELECT [SA_NAME] ,[SA_DEPT] ,[SA_AREA] ,[SA_PHONE] ,[SA_EMAIL] ,[SA_DATAUP] ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_APP_SA_CONTACT_INFO] ' + \
                        ' ORDER BY [SA_AREA], [SA_DEPT], [SA_NAME] '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            # strDATAUP = ss ,[SA_FILEUP]
            # SA_FILEUP = ss, SA_FILEUP
            for (SA_NAME, SA_DEPT, SA_AREA, SA_PHONE, SA_EMAIL, SA_DATAUP) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] \n' + \
                                str(SA_NAME) + ', ' + str(SA_DEPT) + ', ' + str(SA_AREA) + '\n' + \
                                '  公務機號碼: ' + str(SA_PHONE) + '\n' + \
                                '  E-Mail: ' + str(SA_EMAIL) + '\n' + \
                                '  更新日期: ' + str(SA_DATAUP) + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('夜點晚餐' in temp_message.upper()):
        strTitle = 'TOYO夜點晚餐'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            strSQL = 'SELECT [FOOD_KIND] ,[FOOD_NAME] ,[FOOD_STKNUM] ,[FOOD_DAYNUM] ,[FOOD_YN] ,[FOOD_USEDAY] ,[FOOD_CHGYN] ,[FOOD_UPDATE] ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_APP_GA_FOOD_LIST] ' + \
                        ' ORDER BY [FOOD_YN] DESC, [FOOD_USEDAY], [FOOD_KIND], [FOOD_NAME] '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (FOOD_KIND, FOOD_NAME, FOOD_STKNUM, FOOD_DAYNUM, FOOD_YN, FOOD_USEDAY, FOOD_CHGYN, FOOD_UPDATE) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] (' + str(FOOD_KIND) + ') ' + str(FOOD_NAME) + '：' + str(FOOD_YN) + '\n' + \
                                '  可用估：' + str(FOOD_USEDAY) + '天, ' + str(FOOD_CHGYN) + '\n' + \
                                '  庫存:' + str(FOOD_STKNUM) + ', 限量: ' + str(FOOD_DAYNUM) + '\n' + \
                                '  更新日期: ' + str(FOOD_UPDATE) + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('防疫群組' in temp_message.upper()):
        strTitle = 'TOYO防疫群組7天內'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            strSQL = 'SELECT [AF_DAY] ,[PV_DATE] ,[PV_TIME] ,[PV_NAME] ,[PV_NUM] ,[TY_MEM] ,[PV_ISEAT] ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_APP_PV_IN_7_DAY] ' + \
                        ' ORDER BY [PV_DATE], [PV_TIME], [PV_NAME], [TY_MEM]'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (AF_DAY, PV_DATE, PV_TIME, PV_NAME, PV_NUM, TY_MEM, PV_ISEAT) in resList:
                intCount += 1
                if str(AF_DAY) == '當天':
                    strTemp += '[' + str(intCount) + ']' + '當天' + ', ' + str(PV_DATE) + '\n  ' + str(PV_TIME) + ', ' + str(PV_NAME) + ', ' + \
                                    '  ' + str(PV_NUM) + '人\n  陪同：' + str(TY_MEM) + ', ' + '(用餐:)' + str(PV_ISEAT) + '\n\n'
                else:
                    strTemp += '[' + str(intCount) + ']還有' + str(AF_DAY) + '天, ' + str(PV_DATE) + '\n  ' + str(PV_TIME) + ', ' + str(PV_NAME) + ', ' + \
                                    '  ' + str(PV_NUM) + '人\n  陪同：' + str(TY_MEM) + ', ' + '(用餐:)' + str(PV_ISEAT) + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('體溫回報' in temp_message.upper()):
        strTitle = 'TOYO體溫回報(當天)'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            resList = ms.RS_SQL_ExecQuery('SELECT ID, NAME, BT, CHK FROM TIM_DB.dbo.VIEW_APP_MEM_BODYTEMP ORDER BY BT DESC, ID')
            intCount=0
            strTemp=''
            for (ID, NAME, BT, CHK) in resList:
                strTemp = strTemp + str(ID) + ',' + str(NAME) + ',' + str(BT) + ',' + str(CHK) + '\n'
                intCount += 1
            get_message = 'TOYO體溫回報清單：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = 'TOYO體溫回報清單：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \
            ('120' in temp_message.upper() or \
            '$' in temp_message.upper() or \
            'MONEY' in temp_message.upper() or \
            '零用金' in temp_message.upper()):
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        get_message = strMoneyText

    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \
            ('DOOR' in temp_message.upper() or \
            '門禁' in temp_message.upper()):
        strTitle = 'TOYO門禁清單(最新)'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            strSQL = 'SELECT TOP(50) HRM_Dept_Name, HRM_USER_NAME, DoorText, DrDateTime ' + \
                        ' FROM TIM_DB.dbo.VIEW_DOOR_INFO_INSIDE_List ' + \
                        ' ORDER BY DrDateTime DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (HRM_Dept_Name, HRM_USER_NAME, DoorText, DrDateTime) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + ']' + str(DrDateTime) + '\n..' + str(HRM_Dept_Name) + ', ' + str(HRM_USER_NAME) + ', ' + str(DoorText) + '\n'
            get_message = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \
            ('FE' in temp_message.upper() or \
            '滅火' in temp_message.upper()):
        strTitle = 'TOYO 廠區滅火器最近1個月清點情況'
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        if strSQL_FW_Switch == 'ON':
            strTemp=''

            ms = MSSQL(host='211.23.242.222', port='2255', user='sa', pwd='00000', db='TIM_DB')
            strSQL = 'SELECT [FE_TIME] ,[FE_EQNAME] ,[CHK_01] ,[CHK_02] ,[CHK_03] ,[CHK_04] ,[FE_NAME] ' \
                        ' FROM [toyo_web].[dbo].[VIEW_APP_FE_EQ_CHK_NG_List01] ' + \
                        ' ORDER BY FE_TIME DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            for (FE_TIME, FE_EQNAME, CHK_01, CHK_02, CHK_03, CHK_04, FE_NAME) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(FE_TIME) + '\n  ' + str(FE_EQNAME) + '\n  ' + str(CHK_01) + '\n  ' + str(CHK_02) + '\n  ' + \
                             str(CHK_03) + '\n  ' + str(CHK_04) + '\n  檢查人：' + str(FE_NAME) + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp + '\n' + \
                            '以上為有（不合格）品項滅火器\n\n'
                            ' ============================== \n\n'

            strSQL = 'SELECT [FE_TIME] ,[FE_EQNAME] ,[CL-A01] AS CLA01 ,[FE_NAME] ' \
                        ' FROM [toyo_web].[dbo].[VIEW_APP_FE_EQ_CHK_OK_List01] ' + \
                        ' ORDER BY FE_TIME DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            for (FE_TIME, FE_EQNAME, CLA01, FE_NAME) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(FE_TIME) + '\n  ' + str(FE_EQNAME) + '\n  ' + str(CLA01) + '\n  檢查人：' + str(FE_NAME) + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            datNow  + '\n\n' + \
                            strTemp + '\n' + \
                            '以上為（全合格）品項滅火器'
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (temp_message[0:2].upper() == 'TY' or temp_message[0:4].upper() == 'TOYO') and \
            ('MEMO' in temp_message.upper()):
        get_TYPE_message = 'TY_TEXT_Send_MSG'
        get_message = strMemo

    elif (temp_message[0:5].upper() == 'ECTOR') and ('官方帳號教學' in temp_message):
        get_message = strLessonLearning
    # ***** ***** ***** ***** *****

    ##### (Ver)版本 #####
    elif temp_message.upper().count('VER') > 0:
        get_message = '『TOYO行政管理部』版本：\n' + strVer
    # ***** ***** ***** ***** *****

    else:
        get_TYPE_message = 'TSVI非關鍵字的留言'
        get_message = strHowToUse


# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====

    # Send To Line
    if get_TYPE_message == 'Initial':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'TSVI推播程式管理員':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

        # lineNotifyMessage(token, message)        
        #文字訊息
        # reply = TextSendMessage(text=f"{get_message}")
        # line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'TSVI2Ector':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2智弘':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 智弘權杖：
        token = strJohnboToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2冠伶':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 冠伶權杖：
        token = strGwenToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2昆霖':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 昆霖權杖：
        token = strKunToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2宜庭':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 宜庭權杖：        
        token = strMichelleToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI推播全部':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # 智弘權杖：
        token = strJohnboToken
        lineNotifyMessage(token, message)
        # 冠伶權杖：
        token = strGwenToken
        lineNotifyMessage(token, message)
        # 昆霖權杖：
        token = strKunToken
        lineNotifyMessage(token, message)
        # 宜庭權杖：        
        token = strMichelleToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI非關鍵字的留言':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        # message = get_message
        message = 'TOYO行政管理部有留言如下：\n' + temp_message

        if strPush_NotKeyWord2All_Switch == 'ON': 
            # EctorLiu權杖：
            token = strEctorToken
            lineNotifyMessage(token, message)
            # 智弘權杖：
            token = strJohnboToken
            lineNotifyMessage(token, message)
            # 冠伶權杖：
            token = strGwenToken
            lineNotifyMessage(token, message)
            # 昆霖權杖：
            token = strKunToken
            lineNotifyMessage(token, message)
            # 宜庭權杖：        
            token = strMichelleToken
            lineNotifyMessage(token, message)
        else:
            # EctorLiu權杖：
            message = 'DebugModeForEctor\n：' + message
            token = strEctorToken
            lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'How_To_Use':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'New_Activity':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'TY_LOGO':
        reply = ImageSendMessage(original_content_url = 'https://github.com/EctorLiu/Ector01/raw/main/img/A.jpg', \
                                 preview_image_url = 'https://raw.githubusercontent.com/EctorLiu/Ector01/main/img/A.jpg')
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'TY_TEXT_Send_MSG':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'TSVI樣版':
        reply = TemplateSendMessage(alt_text='樣版：需使用手機版方可顯示', \
                    template=ButtonsTemplate( \
                    title='標題：標題說明', \
                    text='樣版可以傳送文字、網址', \
                    actions=[MessageTemplateAction(label='最近活動', text='最近活動'), \
                             URITemplateAction(label='新吉工業區之動畫介紹', \
                             uri='https://www.youtube.com/watch?v=THMFMCY65co&ab_channel=%E5%8F%B0%E5%8D%97%E5%B8%82%E5%B7%A5%E5%95%86%E7%99%BC%E5%B1%95%E6%8A%95%E8%B3%87%E7%AD%96%E9%80%B2%E6%9C%83' ), \
                             PostbackTemplateAction(label='最近活動2', text='最近活動2', data='postback1') \
                    ] \
                ) \
        )
        line_bot_api.reply_message(event.reply_token, reply)

    else:
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)


# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====

# 推播相關部分
def lineNotifyMessage(token, msg):
    headers = {
      'Authorization': 'Bearer ' + token, 
      'Content-Type' : 'application/x-www-form-urlencoded'
    }
    payload = {'message': msg}
    r = requests.post('https://notify-api.line.me/api/notify', headers = headers, params = payload)
    return r.status_code

    # ***** ***** ***** *****  *****

    ##### SQL ######
import pymssql

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

