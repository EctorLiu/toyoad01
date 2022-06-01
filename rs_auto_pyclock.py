    ##### 匯入函式庫 ######
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

import urllib.request
    # ***** ***** ***** ***** *****

    ##### 時間函數 ######
from datetime import datetime
import time
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

    ##### 自訂函數功能 ######
from rm_initial import *
from ri_text_01 import *
from ri_parameters_01 import *
from rf_string_01 import *
from rf_string_02 import *
from rf_datetime_01 import *
import rf_sqldb_01 as pymsdb
from rf_sqldb_02 import *
from rf_line_01 import *
    # ***** ***** ***** ***** *****

    ##### 自動執行程式 ######
@sched.scheduled_job('cron', hour = 7, minute= 50)
@sched.scheduled_job('cron', hour = 8, minute= 30)
@sched.scheduled_job('cron', hour = 9, minute= 30)
@sched.scheduled_job('cron', hour = 10, minute= 30)
@sched.scheduled_job('cron', hour = 11, minute= 30)
@sched.scheduled_job('cron', hour = 12, minute= 30)
@sched.scheduled_job('cron', hour = 13, minute= 30)
@sched.scheduled_job('cron', hour = 14, minute= 30)
@sched.scheduled_job('cron', hour = 15, minute= 30)
@sched.scheduled_job('cron', hour = 16, minute= 30)
@sched.scheduled_job('cron', hour = 17, minute= 30)
@sched.scheduled_job('cron', hour = 18, minute= 30)
@sched.scheduled_job('cron', hour = 19, minute= 30)
@sched.scheduled_job('cron', hour = 20, minute= 30)

def scheduled_job():
    import openpyxl
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pandas as pd

    # 取得當下時間
    FVdatNow = datetime.now()
    FVstrToday = FVdatNow.strftime("%Y-%m-%d") 
    FVstrNow = FVdatNow.strftime("%Y-%m-%d %H:%M:%S") 

    # 連線
    auth_json_path = 'GCP-TOYOAD.json'
    gss_scopes = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path, gss_scopes)
    gss_client = gspread.authorize(credentials)

    # 開啟 Google Sheet 資料表
    MySheet_KEY = '1IgWoZ8uqR2M96AbFm_C2fGCg6Nt9Jp6XjAnrmkgqJIg'
    MySheet_NAME01 = '表單回應 1'
    GLEsheet = gss_client.open_by_key(MySheet_KEY).worksheet(MySheet_NAME01)
    values = GLEsheet.get_all_values()
    dfGLEsheet = pd.DataFrame(values)

    # 資料處理
    strReply_MSG = '現在時間：' + FVstrNow + '\n'
    strTemp = ''
    lngLastRow = len(dfGLEsheet.index)
    lngCount = 1
    strDATADateTime = str(dfGLEsheet.at[lngLastRow - lngCount , 0])
    strDATADateTime = strDATADateTime.replace('上午','am')
    strDATADateTime = strDATADateTime.replace('下午','pm')
    datDATADateTime = datetime.strptime(strDATADateTime, "%Y/%m/%d %p %H:%M:%S")
    if FVdatNow.hour == 7:
        while (FVdatNow - strDATADateTime).seconds <= 50400:
            strDATADateTime = str(dfGLEsheet.at[lngLastRow - lngCount , 0])
            strDATADateTime = strDATADateTime.replace('上午','am')
            strDATADateTime = strDATADateTime.replace('下午','pm')
            datDATADateTime = datetime.strptime(strDATADateTime, "%Y/%m/%d %p %H:%M:%S")
            strTemp += '[' + str(lngCount) + '] 資料時間：\n' + str(datDATADateTime) + '\n' + \
                    '=>部門姓名：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 1]) + ' ' + str(dfGLEsheet.at[lngLastRow - lngCount , 2]) + '\n' + \
                    '=>狀態：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 3]) + '\n' + \
                    '=>檢驗：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 24]) + '\n\n' + \
                    '...................................\n'
            lngCount = lngCount + 1

        if len(strTemp) >= GVintMaxLineMSGString:
            strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
        elif len(strTemp) == 0:
            strTemp += '前1天下班後，無Google防疫回報'
    else:
        while (FVdatNow - datDATADateTime).seconds <= 3600:
            strDATADateTime = str(dfGLEsheet.at[lngLastRow - lngCount , 0])
            strDATADateTime = strDATADateTime.replace('上午','am')
            strDATADateTime = strDATADateTime.replace('下午','pm')
            datDATADateTime = datetime.strptime(strDATADateTime, "%Y/%m/%d %p %H:%M:%S")
            strTemp += '[' + str(lngCount) + '] 資料時間：\n' + str(datDATADateTime) + '\n' + \
                    '=>部門姓名：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 1]) + ' ' + str(dfGLEsheet.at[lngLastRow - lngCount , 2]) + '\n' + \
                    '=>狀態：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 3]) + '\n' + \
                    '=>檢驗：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 24]) + '\n\n' + \
                    '...................................\n'
            lngCount = lngCount + 1

        if len(strTemp) >= GVintMaxLineMSGString:
            strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
        elif len(strTemp) == 0:
            strTemp += '前1小時內，無Google防疫回報'

    strReply_MSG += strTemp
    # ***** ***** ***** ***** *****
    # ECTOR_ID：Ua42052df655d4d9538b864a3c4deaf28
    # 測試群組ID：Cff5125a1ea645aa836eb7de5511d2b89
    # VBA群組ID：Cdf7c089f566a65261a84ae4a16d9afb4
    # 防疫群組ID：C8df0a16b1b940252195b00280db2fa75
    # 菲尼克斯群組ID：Cdd617a7f3515934d7c75e1d00c4f3605
    # HR_職安衛ID：C2dc8eb757a1b585721a21f8a3aa73853
    line_bot_api.push_message('Ua42052df655d4d9538b864a3c4deaf28',TextSendMessage(text=strReply_MSG))
    line_bot_api.push_message('Cdf7c089f566a65261a84ae4a16d9afb4',TextSendMessage(text=strReply_MSG))
    line_bot_api.push_message('Cff5125a1ea645aa836eb7de5511d2b89',TextSendMessage(text=strReply_MSG))
    # url = 'https://toyoad01.herokuapp.com/'
    # conn = urllib.request.urlopen(url)
    # for key, value in conn.getheaders():
    #     print(key, value)

sched.start()
    # ***** ***** ***** ***** *****


    ##### 備註區域 ######
# 表示2017年3月22日17时19分07秒执行该程序
# sched.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)
 
# 表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
# sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
 
# 表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
# ched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')
 
# 表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
# sched.add_job(my_job, 'cron',second = '*/5')

# @sched.scheduled_job('cron', day_of_week = 'mon-fri', hour = 11, minute = 35, second = 05)
# @sched.scheduled_job('cron', year = 2021, month = 12, day = 27, hour = 12, minute = 2, second = 30)

# @sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/25')
# @sched.scheduled_job('cron', year = 2021, month = 12, day = 25, minute = 20)
    # ***** ***** ***** ***** *****
