    ##### INDEX ######
# GVstrHowToUse: 如何使用
# GVstrSOPList01: SOP選單資料
# GVstrMemo: 備註住址導航
# GVstrLessonLearning: 官方帳號教學
# GVstrLineNotifyHowToGetToken: 如何取得權杖
# GVstrCMKeyWord: 關鍵字清單CM
# GVstrECKeyWord: 關鍵字清單EC
    # ***** ***** ***** ***** *****


    ##### 如何使用 ######
GVstrHowToUse = '『TOYO行政管理部』：\n' + \
                'Hi！這是行政管理部之官方帳號！\n謝謝你的訊息！\n\n' + \
                '也許您可用下述常用關鍵字查詢：\n' + \
                '「面試報到」\n' + \
                '「業務電話」\n' + \
                '「夜點晚餐」\n' + \
                '「防疫群組」\n' + \
                '「體溫回報」\n' + \
                '「如何使用」\n' + \
                '「最新訊息」等..'
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

    ##### MEMO ######
GVstrMemo = '公司住址：70947台南市安南區新吉三路55號\n' + \
            '導航：https://g.page/TOYOROBOT?share'
    # ***** ***** ***** ***** *****

    ##### 官方帳號教學 ######
GVstrLessonLearning = 'A1. 申請官方帳號：\n' + \
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
                '[推播功能]\n' + \
                '(TY or TOYO) + \n' + \
                '*(1)推播ECTOR + 內容\n' + \
                '*(2)推播智弘 + 內容\n' + \
                '*(3)推播冠伶 + 內容\n' + \
                '*(4)推播昆霖 + 內容\n' + \
                '*(5)推播汶靜 + 內容\n' + \
                '*(6)推播宜庭 + 內容\n' + \
                '*(7)推播玉敏 + 內容\n' + \
                '*(8)推播MOMO + 內容\n' + \
                '*(9)推播全部 + 內容\n' + \
                '\n' + \
                '[關鍵字]\n' + \
                '(1)如何使用/HELP/?/？\n' + \
                '(2)(最近 or 最新) + (訊息 or 活動)\n' + \
                '(3)(SOP) + (清單 or 下載)\n' + \
                '\n' + \
                '[資料庫]\n' + \
                '*(1)(宿舍) + (防疫) + (房間 or 人名)\n' + \
                '*(2)(車輛 or 車道) + (查詢) + (車牌 or 人名)\n' + \
                '*(3)面試報到\n' + \
                '*(4)業務電話\n' + \
                '*(5)夜點晚餐\n' + \
                '*(6)防疫群組\n' + \
                '*(7)體溫回報\n' + \
                '\n' + \
                '[內部使用]\n' + \
                '*(1)(TY or TOYO) + (DOOR or 門禁)\n' + \
                '*(2)(TY or TOYO) + (NEWFE or 新滅火)\n' + \
                '*(3)(TY or TOYO) + (FE or 滅火)\n' + \
                '*(4)(TY or TOYO) + (MEMO)\n' + \
                '\n' + \
                '[教學]\n' + \
                '(1)(TY or TOYO) + (推播權杖教學)\n' + \
                '(2)(TY or TOYO) + (官方帳號教學)\n' + \
                ''
    # ***** ***** ***** ***** *****

    ##### 關鍵字清單 ######
GVstrECKeyWord = 'KW：\n' + \
                '[開放使用]\n' + \
                '(1)(SOP) + (清單 or 下載)\n' + \
                '\n' + \
                '[推播功能]\n' + \
                '(TY or TOYO) + \n' + \
                '*(1)推播ECTOR + 內容\n' + \
                '*(2)推播智弘 + 內容\n' + \
                '*(3)推播冠伶 + 內容\n' + \
                '*(4)推播昆霖 + 內容\n' + \
                '*(5)推播汶靜 + 內容\n' + \
                '*(6)推播宜庭 + 內容\n' + \
                '*(7)推播玉敏 + 內容\n' + \
                '*(8)推播MOMO + 內容\n' + \
                '*(9)推播全部 + 內容\n' + \
                '\n' + \
                '[關鍵字]\n' + \
                '(1)如何使用/HELP/?/？\n' + \
                '(2)(最近 or 最新) + (訊息 or 活動)\n' + \
                '(3)(SOP) + (清單 or 下載)\n' + \
                '\n' + \
                '[資料庫]\n' + \
                '*(1)(宿舍) + (防疫) + (房間 or 人名)\n' + \
                '*(2)(車輛 or 車道) + (查詢) + (車牌 or 人名)\n' + \
                '*(3)面試報到\n' + \
                '*(4)業務電話\n' + \
                '*(5)夜點晚餐\n' + \
                '*(6)防疫群組\n' + \
                '*(7)體溫回報\n' + \
                '\n' + \
                '[內部使用]\n' + \
                '*(1)(TY or TOYO) + (DOOR or 門禁)\n' + \
                '*(2)(TY or TOYO) + (NEWFE or 新滅火)\n' + \
                '*(3)(TY or TOYO) + (FE or 滅火)\n' + \
                '*(4)(TY or TOYO) + (MEMO)\n' + \
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
                '(1)E.4. + HN + (KW or LINE)\n' + \
                ''
    # ***** ***** ***** ***** *****
