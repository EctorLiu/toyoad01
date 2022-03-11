    ##### INDEX ######
# def RS_lineNotifyMessage(token, msg): 推播訊息至指定的TOKEN
    # ***** ***** ***** ***** *****


    ##### 匯入函式庫 ######
import requests
    # ***** ***** ***** ***** *****


    ##### 推播相關部分 ######
def RS_lineNotifyMessage(token, msg):
    headers = {
      "Authorization": "Bearer " + token, 
      "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
    # ***** ***** ***** ***** *****
