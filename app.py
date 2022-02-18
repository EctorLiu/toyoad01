# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====

    ##### 版本 ######
strVer = '(M218)1130'

    # 切換SQL功能選擇：ON/OFF
strSQL_FW_Switch = 'ON'
    # 切換同仁推播功能選擇：ON/OFF
strPush_NotKeyWord2All_Switch = 'ON'
    # ***** ***** ***** ***** *****

    ##### 限制 ######
intMaxLineMSGString = 4900
intMaxItemString = 200
    # ***** ***** ***** ***** *****

    ##### 預設留言 ######
strNewestActivity = '『TOYO行政管理部』：最近活動\n' + \
                '更新：2022/01/17 17:20 ...\n\n' + \
                '..'

    # ***** ***** ***** ***** *****

    ##### (TSVI)推播 ######
import requests
    # ***** ***** ***** ***** *****

    ##### 時間函數 ######
from datetime import datetime
import time

FVdatNow = datetime.now()
FVstrToday = FVdatNow.strftime("%Y-%m-%d") 
FVstrNow = FVdatNow.strftime("%Y-%m-%d %H:%M:%S") 

# FVstrLCNow = time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime())
FVstrGMNow = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
FVdatGMNow = datetime.strptime(FVstrGMNow, "%Y-%m-%d %H:%M:%S") 
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
    strEventMSG = event.message.text

    ##### 全型符號轉換 #####
    strEventMSG = strEventMSG.replace('！','!')
    strEventMSG = strEventMSG.replace('（','(')
    strEventMSG = strEventMSG.replace('）',')')
    strEventMSG = strEventMSG.replace('，',',')
    strEventMSG = strEventMSG.replace('＄','$')
    strEventMSG = strEventMSG.replace('？','?')
    # ***** ***** ***** ***** *****

    ##### 關鍵字處理大寫消空白 #####
    strEventMSG = strEventMSG.upper()
    strEventMSG = strEventMSG.strip()
    # ***** ***** ***** ***** *****

    # 確認資料類別
    get_TYPE_message = 'Initial'

    if strEventMSG == '您好':
        # (A)禮貌回覆
        strReply_MSG = '『TOYO行政管理部』：您好' + event.message.text

    ##### (TSVI)推播 #####
    elif (strEventMSG[0:4].upper() == 'TY推播' or strEventMSG[0:6].upper() == 'TOYO推播'):
        #類別
        get_TYPE_message = 'SYS_ASSIGN_PUSH_MSG_Text'
        #開頭的關鍵字長度
        if strEventMSG[0:4].upper() == 'TY推播':
            intInitialKWLen = 4
        elif strEventMSG[0:6].upper() == 'TOYO推播':
            intInitialKWLen = 6
        strPushKW = RS_RIGHT_String_NotLeftStrNum(strEventMSG, intInitialKWLen)
        #strReply_MSG
        if (strPushKW[0:5].upper() == 'ECTOR'):
            intKWLength = 5
            strPush2Who = strEctorToken
            strStartInfo = '(只推Ector)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '智弘'):
            intKWLength = 2
            strPush2Who = strJohnboToken
            strStartInfo = '(只推智弘)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '冠伶'):
            intKWLength = 2
            strPush2Who = strGwenToken
            strStartInfo = '(只推冠伶)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '昆霖'):
            intKWLength = 2
            strPush2Who = strKunToken
            strStartInfo = '(只推昆霖)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '汶靜'):
            intKWLength = 2
            strPush2Who = strJingToken
            strStartInfo = '(只推汶靜)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '宜庭'):
            intKWLength = 2
            strPush2Who = strMichelleToken
            strStartInfo = '(只推宜庭)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '玉敏'):
            intKWLength = 2
            strPush2Who = strMinToken
            strStartInfo = '(只推玉敏)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:4].upper() == 'MOMO'):
            intKWLength = 4
            strPush2Who = strMomoToken
            strStartInfo = '(只推MOMO)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
        if (strPushKW[0:2].upper() == '全部'):
            intKWLength = 2
            strPush2Who = 'SYS_PUSH_ALL'
            strStartInfo = '(推全部)\n'
            strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
    # ***** ***** ***** ***** *****

    ##### TSVI樣版 #####
    elif (strEventMSG[0:4].upper() == 'TSVI') and \
            ('樣版' in strEventMSG.upper()):
        get_TYPE_message = 'TSVI樣版'   
    # ***** ***** ***** ***** *****

    ##### 關鍵字 #####
    elif ('如何使用' in strEventMSG or 'HELP' in strEventMSG.upper() or '?' in strEventMSG.strip() or '？' in strEventMSG.strip()):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrHowToUse

    elif ('最近' in strEventMSG or '最新' in strEventMSG) and ('訊息' in strEventMSG or '活動' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = strNewestActivity

    elif ('SOP' in strEventMSG) and ('清單' in strEventMSG or '下載' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrSOPList01

    elif ('宿舍' in strEventMSG) and \
            ('防疫' in strEventMSG):
        if len(strEventMSG) == 4:
            strCond = '\'%\''
        else:
            strCond = strEventMSG
            strCond = strCond.replace('宿舍', '')
            strCond = strCond.replace('防疫', '')
            strCond = '\'%' + strCond.strip() + '%\''
        strTitle = 'TOYO移工宿舍輪班查詢(前3天到今天)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            #DeptName MemName ShiftResult   DormPos
            #裝配課    陳文水  08~17_T休息班 (長宏)公學宿舍_3F_301
            strSQL = 'SELECT [DeptName], [MemName], [ShiftResult], [DormPos], FILETIME ' + \
                        ' FROM [APP_AGENT_Foreign_R1_Check_Dorm_Shift_List]' + \
                        ' WHERE ([MemName] LIKE %s OR [DormPos] LIKE %s) '  % (strCond, strCond) + \
                        ' ORDER BY DormPos, MemName DESC '            
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (DeptName, MemName, ShiftResult, DormPos, FILETIME) in resList:
                strFileName = str(FILETIME)
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(DeptName) + ',' + str(MemName) + '\n' + \
                            str(DormPos) + '\n' + \
                            str(ShiftResult).replace(',', '\n').strip() + '\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '..現在時間：' + FVstrNow  + '\n' + \
                            '..檔案更新：' + strFileName  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('車輛' in strEventMSG or '車道' in strEventMSG) and \
            ('查詢' in strEventMSG):
        if len(strEventMSG) == 4:
            strCond = '\'%\''
        else:
            strCond = strEventMSG
            strCond = strCond.replace('車輛', '')
            strCond = strCond.replace('車道', '')
            strCond = strCond.replace('查詢', '')
            strCond = '\'%' + strCond.strip() + '%\''
        strTitle = 'TOYO車輛申請查詢(車牌/姓名)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT [DEPT_NAME], [MEM_NAME], [CAR_LIST] ' + \
                        ' FROM [TIM_DB].[dbo].[APP_BPM_TNFAB01_R1_MEM_CAR_OKLIST] ' + \
                        ' WHERE ([CAR_LIST] LIKE %s OR [CAR_LISTX] LIKE %s OR [MEM_NAME] LIKE %s) '  % (strCond, strCond, strCond) + \
                            ' AND (LEN([CAR_LIST]) > 0) ' + \
                        ' ORDER BY CAR_LIST '            
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (DEPT_NAME, MEM_NAME, CAR_LIST) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + '車輛：\n' + \
                            str(CAR_LIST).replace(',', '\n').strip() + '\n' + \
                            '..員工：(' + str(DEPT_NAME) + ')' + str(MEM_NAME) + '\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('面試報到' in strEventMSG):
        strTitle = 'TOYO面試報到10天內'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
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
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('業務電話' in strEventMSG):
        strTitle = 'TOYO業務電話'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT [SA_NAME] ,[SA_DEPT] ,[SA_AREA] ,[SA_PHONE] ,[SA_EMAIL] ,[SA_DATAUP] ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_APP_SA_CONTACT_INFO] ' + \
                        ' ORDER BY [SA_AREA] DESC, [SA_DEPT], [SA_NAME] '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SA_NAME, SA_DEPT, SA_AREA, SA_PHONE, SA_EMAIL, SA_DATAUP) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] \n' + \
                                str(SA_NAME) + ', ' + str(SA_DEPT) + ', ' + str(SA_AREA) + '\n' + \
                                '  公務機號碼: ' + str(SA_PHONE) + '\n' + \
                                '  E-Mail: ' + str(SA_EMAIL) + '\n' + \
                                '  更新日期: ' + str(SA_DATAUP) + '\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('夜點晚餐' in strEventMSG):
        strTitle = 'TOYO夜點晚餐'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
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
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('防疫群組' in strEventMSG):
        strTitle = 'TOYO防疫群組7天內'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
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
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
    elif ('體溫回報' in strEventMSG):
        strTitle = 'TOYO體溫回報(當天)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            resList = ms.RS_SQL_ExecQuery('SELECT DISTINCT ID, NAME, BT, CHK FROM TIM_DB.dbo.VIEW_APP_MEM_BODYTEMP ORDER BY BT DESC, ID')
            intCount=0
            strTemp=''
            for (ID, NAME, BT, CHK) in resList:
                strTemp = strTemp + str(ID) + ',' + str(NAME) + ',' + str(BT) + ',' + str(CHK) + '\n'
                intCount += 1
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = 'TOYO體溫回報清單：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = 'TOYO體溫回報清單：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('120' in strEventMSG or \
            '$' in strEventMSG or \
            'MONEY' in strEventMSG.upper() or \
            '零用金' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrMoneyText

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('DOOR' in strEventMSG.upper() or \
            '門禁' in strEventMSG):
        strTitle = 'TOYO門禁清單(最新)'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT TOP(50) HRM_Dept_Name, HRM_USER_NAME, DoorText, DrDateTime ' + \
                        ' FROM TIM_DB.dbo.VIEW_DOOR_INFO_INSIDE_List ' + \
                        ' ORDER BY DrDateTime DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (HRM_Dept_Name, HRM_USER_NAME, DoorText, DrDateTime) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + ']' + str(DrDateTime) + '\n..' + str(HRM_Dept_Name) + ', ' + str(HRM_USER_NAME) + ', ' + str(DoorText) + '\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('NEWFE' in strEventMSG.upper() or \
            '新滅火' in strEventMSG):
        strTitle = 'TOYO 廠區滅火器最近1次清點情況'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT [FE_TIME] ,[FE_EQNAME] ,[CHK_01] ,[CHK_02] ,[CHK_03] ,[CHK_04] ,[FE_NAME] ' \
                        ' FROM [toyo_web].[dbo].[VIEW_APP_FE_EQ_CHK_NewestNGList01] ' + \
                        ' ORDER BY FE_TIME DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (FE_TIME, FE_EQNAME, CHK_01, CHK_02, CHK_03, CHK_04, FE_NAME) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(FE_TIME) + '\n  ' + str(FE_EQNAME) + '\n  ' + str(CHK_01) + '\n  ' + str(CHK_02) + '\n  ' + \
                             str(CHK_03) + '\n  ' + str(CHK_04) + '\n  檢查人：' + str(FE_NAME) + '\n\n'
            strContent = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp + '\n' + \
                            '  以上為有（不合格）品項滅火器\n' + \
                            ' ============================== \n\n'

            strSQL = 'SELECT [FE_TIME] ,[FE_EQNAME] ,[CHK_00] ,[FE_NAME] ' \
                        ' FROM [toyo_web].[dbo].[VIEW_APP_FE_EQ_CHK_NewestOKList01] ' + \
                        ' ORDER BY FE_TIME DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (FE_TIME, FE_EQNAME, CHK_00, FE_NAME) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(FE_TIME) + '\n  ' + str(FE_EQNAME) + '\n  ' + str(CHK_00) + '\n  檢查人：' + str(FE_NAME) + '\n\n'
            strContent = strContent + strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp + '\n' + \
                            '以上為（全合格）品項滅火器\n' + \
                            ' ============================== '
            if len(strContent) >= intMaxLineMSGString:
                strContent = strContent[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strContent
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('FE' in strEventMSG.upper() or \
            '滅火' in strEventMSG):
        strTitle = 'TOYO 廠區滅火器最近1個月清點情況'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT [FE_TIME] ,[FE_EQNAME] ,[CHK_01] ,[CHK_02] ,[CHK_03] ,[CHK_04] ,[FE_NAME] ' \
                        ' FROM [toyo_web].[dbo].[VIEW_APP_FE_EQ_CHK_NG_List01] ' + \
                        ' ORDER BY FE_EQNAME'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (FE_TIME, FE_EQNAME, CHK_01, CHK_02, CHK_03, CHK_04, FE_NAME) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(FE_TIME) + '\n  ' + str(FE_EQNAME) + '\n  ' + str(CHK_01) + '\n  ' + str(CHK_02) + '\n  ' + \
                             str(CHK_03) + '\n  ' + str(CHK_04) + '\n  檢查人：' + str(FE_NAME) + '\n\n'
            strContent = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp + '\n' + \
                            '  以上為有（不合格）品項滅火器\n' + \
                            ' ============================== \n\n'

            strSQL = 'SELECT [FE_TIME] ,[FE_EQNAME] ,[CL-A01] AS CLA01 ,[FE_NAME] ' \
                        ' FROM [toyo_web].[dbo].[VIEW_APP_FE_EQ_CHK_OK_List01] ' + \
                        ' ORDER BY FE_EQNAME'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (FE_TIME, FE_EQNAME, CLA01, FE_NAME) in resList:
                intCount += 1
                strTemp += '[' + str(intCount) + '] ' + str(FE_TIME) + '\n  ' + str(FE_EQNAME) + '\n  ' + str(CLA01) + '\n  檢查人：' + str(FE_NAME) + '\n\n'
            strContent = strContent + strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + \
                            FVstrNow  + '\n\n' + \
                            strTemp + '\n' + \
                            '以上為（全合格）品項滅火器\n' + \
                            ' ============================== '
            if len(strContent) >= intMaxLineMSGString:
                strContent = strContent[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strContent
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('MEMO' in strEventMSG.upper()):
        if RS_CHECK_KWAUTH_by_UserId[0:2] == 'OK':
            get_TYPE_message = 'SYS_KW_INPUT_MSG'
            strReply_MSG = GVstrMemo
        else:
            get_TYPE_message = 'SYS_KW_INPUT_MSG'
            strReply_MSG = '權限不足!'

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('官方帳號教學' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrLessonLearning

    elif (strEventMSG[0:2].upper() == 'TY' or strEventMSG[0:4].upper() == 'TOYO') and \
            ('推播權杖教學' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrLineNotifyHowToGetToken
    # ***** ***** ***** ***** *****

    ##### (Ver)版本 #####
    elif strEventMSG.upper().count('VER') > 0:
        strReply_MSG = '『TOYO行政管理部』版本：\n' + strVer
    # ***** ***** ***** ***** *****

    ##### 列出全部的關鍵字清單 #####
    elif (strEventMSG[0:4].upper() == 'TOYO') and ('!ALL' in strEventMSG):
        get_TYPE_message = 'Initial'
        #get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrCMKeyWord
    # ***** ***** ***** ***** *****

    ##### 程式開發使用 #####
    elif (strEventMSG[0:5].upper() == 'ECTOR'):
        if len(strEventMSG) == 5:
            strCond = ''
        else:
            strCond = strEventMSG.replace('ECTOR', '')
            strCond = strCond.strip()
        #比對輸入[小時分鐘](1225)
        strHHNN = RS_DateTime_2_HHNN()
        #開發者關鍵字清單
        if (strHHNN in strCond) and ('KW' in strCond):        
            get_TYPE_message = 'SYS_KW_INPUT_MSG'
            strReply_MSG = GVstrECKeyWord
        #官方帳號教學
        elif (strHHNN in strCond) and ('LINE' in strCond):        
            get_TYPE_message = 'SYS_KW_INPUT_MSG'
            strReply_MSG = GVstrLessonLearning
        else:
            get_TYPE_message = 'SYS_KW_INPUT_MSG'
            strReply_MSG = 'EC' + strCond + '\n' * 100 + strHHNN[-2:] + 'OK'

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

    else:
        get_TYPE_message = 'SYS_NOT_KW_INPUT_MSG'
        strReply_MSG = GVstrHowToUse

        
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====

    ##### 取得Line訊息 #####
    pfProfile = line_bot_api.get_profile(event.source.user_id)
    strLineDisplayName = pfProfile.display_name
    strLineUserID = pfProfile.user_id
    # ***** ***** ***** ***** *****

    # #####Send To Line
    if get_TYPE_message == 'Initial':
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****

    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'SYS_ASSIGN_PUSH_MSG_Text':
        #推播訊息編輯
        push_message = '\n來自[' + strLineDisplayName + ']推播訊息：\n' + strReply_MSG
        #推播ALL or 個人
        if strPush2Who == 'SYS_PUSH_ALL':
            # EctorLiu權杖:
            token = strEctorToken
            lineNotifyMessage(token, push_message)
            # 智弘權杖:
            token = strJohnboToken
            lineNotifyMessage(token, push_message)
            # 冠伶權杖:
            token = strGwenToken
            lineNotifyMessage(token, push_message)
            # 昆霖權杖:
            token = strKunToken
            lineNotifyMessage(token, push_message)
            # 汶靜權杖:
            token = strJingToken
            lineNotifyMessage(token, push_message)
            # 宜庭權杖:
            token = strMichelleToken
            lineNotifyMessage(token, push_message)
            # 玉敏權杖:
            token = strMinToken
            lineNotifyMessage(token, push_message)
            # MOMO權杖:
            token = strMomoToken
            lineNotifyMessage(token, push_message)            
        else:
            # 個人:            
            token = strPush2Who
            lineNotifyMessage(token, push_message)
    # ***** ***** ***** ***** *****

    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'SYS_KW_INPUT_MSG':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        #推播訊息編輯
        push_message = '『KeyWord』\nDebugModeForEctor：' + push_message
        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)


    elif get_TYPE_message == 'SYS_NOT_KW_INPUT_MSG':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        if strPush_NotKeyWord2All_Switch == 'ON': 
            # EctorLiu權杖：
            token = strEctorToken
            lineNotifyMessage(token, push_message)
            # 智弘權杖：
            token = strJohnboToken
            lineNotifyMessage(token, push_message)
            # 冠伶權杖：
            token = strGwenToken
            lineNotifyMessage(token, push_message)
            # 昆霖權杖：
            token = strKunToken
            lineNotifyMessage(token, push_message)
            # 汶靜權杖：
            token = strJingToken
            lineNotifyMessage(token, push_message)
            # 宜庭權杖：
            token = strMichelleToken
            lineNotifyMessage(token, push_message)
            # 玉敏權杖：
            token = strMinToken
            lineNotifyMessage(token, push_message)
            # MOMO權杖：
            token = strMomoToken
            lineNotifyMessage(token, push_message)
        else:
            #推播訊息編輯
            push_message = '『非關鍵字』\nDebugModeForEctor：' + push_message
            # EctorLiu權杖：
            token = strEctorToken
            lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****


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
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        #推播訊息編輯
        push_message = '『特殊狀況』\nDebugModeForEctor：' + push_message
        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)

# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====

    # SQL_LOG紀錄
    strEventMSG = strEventMSG.replace("'", '')
    strEventMSG = strEventMSG.replace('"', '')
    strReply_MSG = strReply_MSG.replace("'", '')
    strReply_MSG = strReply_MSG.replace('"', '')
    strSQLReturn = RS_Line_LOG_ADD(strLineDisplayName, strLineUserID, strEventMSG, strReply_MSG)

# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====

    ##### 推播相關部分 ######
def lineNotifyMessage(token, msg):
    headers = {
      'Authorization': 'Bearer ' + token, 
      'Content-Type' : 'application/x-www-form-urlencoded'
    }
    payload = {'message': msg}
    r = requests.post('https://notify-api.line.me/api/notify', headers = headers, params = payload)
    return r.status_code
    # ***** ***** ***** *****  *****


    ##### 日期編碼 ######
def RS_DateTime_2_HHNN():
    datDT = time.localtime()
    strHour = time.strftime("%H", datDT) 
    strMinute = time.strftime("%M", datDT) 
    if len(strHour) < 2:
        strHour = '0' + strHour
    if len(strMinute) < 2:
        strMinute = '0' + strMinute
    RS_DateTime_2_HH_NN = strHour + strMinute
    return RS_DateTime_2_HH_NN
    # ***** ***** ***** ***** *****


    ##### 字串處理 ######
def RS_LEFT_String_StrNum(strTemp, intNum):
    return strTemp[:intNum]

def RS_RIGHT_String_StrNum(strTemp, intNum):
    return strTemp[-intNum:]

def RS_RIGHT_String_NotLeftStrNum(strTemp, intNum):    
    return strTemp[-(len(strTemp)-intNum):]

def RS_MID_String_Start_StrNum(strTemp, intStart, intNum):
    return strTemp[intStart:intStart+intNum]
    # ***** ***** ***** ***** *****


    ##### 權限查詢 ######
def RS_CHECK_KWAUTH_by_UserId(strUserId, strQueryKW):
    #查詢資料
    if strSQL_FW_Switch == 'ON':
        ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' SELECT [AUTH_KW_List],[AUTH_UnitName],[AUTH_MemName] ' + \
                    ' FROM [TIM_DB].[dbo].[tblAPP_TYAD_Auth_List] ' + \
                    ' WHERE ([AUTH_UserID] = %s) '  % (strUserId) '            
        resList = ms.RS_SQL_ExecQuery(strSQL)
        strTemp=''
        for ([AUTH_UnitName],[AUTH_MemName],[AUTH_KW_List]) in resList:
            strAuthUnitName = str(AUTH_UnitName)
            strAuthMemName = str(AUTH_MemName)
            strAuthKWList = str(AUTH_KW_List)
        if ('ALL' in strAuthKWList.upper()):
            RS_CHECK_AUTH_by_UserId = 'GO' + ',' + strAuthUnitName + ',' + strAuthMemName
        elif (strQueryKW.upper() in strAuthKWList.upper()):
            RS_CHECK_AUTH_by_UserId = 'GO' + ',' + strAuthUnitName + ',' + strAuthMemName
        else:
            RS_CHECK_AUTH_by_UserId = 'NG' + ',' + strAuthUnitName + ',' + strAuthMemName

    return RS_CHECK_AUTH_by_UserId

    ##### LineLOG ######
def RS_Line_LOG_ADD(strLineName, strLineUserID, strKeyInMSG, strLineRpMSG):
    #取得時間
    datDT = datetime.now()
    strDateTime = datDT.strftime("%Y-%m-%d %H:%M:%S")

    #寫入LOG
    if strSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_TYAD_LineLog]'
        #連線
        ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' INSERT INTO [TIM_DB].[dbo].[tblAPP_TYAD_LineLog] ' + \
                    ' (EX01, EX02, EX03, TXT01, TXT02, EXDT01) ' + \
                    ' VALUES (\'' + (strDateTime) + '\',\'' + (strLineName) + '\',\'' + (strLineUserID) + '\',\'' + (strKeyInMSG) + '\',\'' + (strLineRpMSG) + \
                                '\',Convert(datetime, \'' + strDateTime + '\',111)) '
        resList = ms.RS_SQL_ExecNonQuery(strSQL)
        RS_Line_LOG = strDateTime + '：寫入DB OK!\n' + \
                        strSQL
        return RS_Line_LOG
    else:
        RS_Line_LOG = 'SQL_2'
        return RS_Line_LOG
    # ***** ***** ***** ***** *****

