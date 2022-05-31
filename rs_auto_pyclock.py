    ##### 匯入函式庫 ######
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

import urllib.request
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
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 7, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 8, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 9, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 10, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 11, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 12, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 13, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 14, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 15, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 16, minute= 30)
@sched.scheduled_job('cron', day_of_week='mon-fri', hour = 17, minute= 30)

@sched.scheduled_job('cron', day_of_week='mon-fri', minute= 35)
@sched.scheduled_job('cron', day_of_week='mon-fri', minute= 36)
@sched.scheduled_job('cron', day_of_week='mon-fri', minute= 37)

def scheduled_job():
    import openpyxl
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pandas as pd

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
    strTemp=''
    lngLastRow = len(dfGLEsheet.index)
    lngCount = 1
    strDATADateTime = str(dfGLEsheet.at[lngLastRow - lngCount , 0])
    strDATADateTime = strDATADateTime.replace('上午','am')
    strDATADateTime = strDATADateTime.replace('下午','pm')
    datDATADateTime = datetime.strptime(strDATADateTime, "%Y/%m/%d %p %H:%M:%S")
    # while (FVdatNow - datDataTime).seconds <= 86400:
    while (FVdatNow - datDATADateTime).seconds <= 10800:
        strDATADateTime = str(dfGLEsheet.at[lngLastRow - lngCount , 0])
        strDATADateTime = strDATADateTime.replace('上午','am')
        strDATADateTime = strDATADateTime.replace('下午','pm')
        datDATADateTime = datetime.strptime(strDATADateTime, "%Y/%m/%d %p %H:%M:%S")
        strTemp = '[' + lngCount + '] 資料時間：\n' + str(datDATADateTime) + '\n' + \
                '=>部門姓名：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 1]) + ' ' + str(dfGLEsheet.at[lngLastRow - lngCount , 2]) + '\n' + \
                '=>狀態：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 3]) + '\n' + \
                '=>檢驗：\n' + str(dfGLEsheet.at[lngLastRow - lngCount , 24]) + '\n\n' + \
                '...................................\n'
        lngCount = lngCount + 1

    if len(strTemp) >= GVintMaxLineMSGString:
        strTemp = strTemp[0:GVintMaxLineMSGString] + '...(資料過多)'
    elif len(strTemp) == 0:
        strTemp = '這段時間內無資料'

    strReply_MSG = strTemp
    # ***** ***** ***** ***** *****
    # 行政官方帳號ID：Ua42052df655d4d9538b864a3c4deaf28
    # 測試群組ID：Ua42052df655d4d9538b864a3c4deaf28
    # 測試群組ID：Cff5125a1ea645aa836eb7de5511d2b89
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
