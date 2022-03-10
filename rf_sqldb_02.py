    ##### INDEX ######
# def RS_CHECK_KWAUTH_by_UserId(strCondUserId, strCondQueryKW): 檢查[LineUniqueID]是否具備[特定功能權限](回傳前兩個字OK/NG)
# def RS_Get_AUTHList_by_UserDBName(strQueryUserDBName): 查詢[資料庫姓名]對應[權限清單]
# def RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineName, strLineUserID, strModUserDBName, strModAUTHItemName, strModYN): 修改[資料庫姓名]對應[權限清單]
# def RS_Line_LOG_ADD(strLineName, strLineUserID, strKeyInMSG, strLineRpMSG): 寫入LOG歷史資料
    # ***** ***** ***** ***** *****


    ##### 自訂函數功能 ######
from rm_initial import *
from ri_parameters_01 import *
import rf_sqldb_01 as pymsdb
from datetime import datetime
import time
    # ***** ***** ***** ***** *****


    ##### LineAUTH ######
def RS_CHECK_KWAUTH_by_UserId(strCondUserId, strCondQueryKW):
    RS_CHECK_KWAUTH_by_UserId = 'INITIAL_STATE'
    #查詢資料
    if GVstrSQL_FW_Switch == 'ON':
        ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' SELECT [AUTH_UnitName],[AUTH_MemName],[AUTH_KW_List] ' + \
                    ' FROM [TIM_DB].[dbo].[tblAPP_TYAD_Auth_List] ' + \
                    ' WHERE ( [AUTH_UserID] = \'' + str(strCondUserId) + '\')'
        resList = ms.RS_SQL_ExecQuery(strSQL)
        strAuthUnitName = 'INI_A'
        strAuthMemName = 'INI_B'
        strAuthKWList = 'INI_C'
        for (AUTH_UnitName, AUTH_MemName, AUTH_KW_List) in resList:
            strAuthUnitName = str(AUTH_UnitName)
            strAuthMemName = str(AUTH_MemName)
            strAuthKWList = str(AUTH_KW_List)

        if ('ALL' in strAuthKWList):
            RS_CHECK_KWAUTH_by_UserId = 'GO' + ',(U)' + strAuthUnitName + ',(M)' + strAuthMemName + ',(A)' + strAuthKWList
        elif (strCondQueryKW.upper() in strAuthKWList):
            RS_CHECK_KWAUTH_by_UserId = 'GO' + ',(U)' + strAuthUnitName + ',(M)' + strAuthMemName + ',(A)' + strAuthKWList
        else:
            RS_CHECK_KWAUTH_by_UserId = 'NG' + ',(U)' + strAuthUnitName + ',(M)' + strAuthMemName + ',(A)' + strAuthKWList

    return RS_CHECK_KWAUTH_by_UserId
    # ***** ***** ***** ***** *****


    ##### LineAUTH ######
def RS_Get_AUTHList_by_UserDBName(strQueryUserDBName):
    #查詢AuthList
    if GVstrSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_TYAD_Auth_List]'
        ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' SELECT [AUTH_KW_List] ' + \
                    ' FROM [TIM_DB].[dbo].[tblAPP_TYAD_Auth_List] ' + \
                    ' WHERE [AUTH_MemName] = \'' + strQueryUserDBName + '\''
        resList = ms.RS_SQL_ExecQuery(strSQL)
        intCount=0
        for (AUTH_KW_List) in resList:
            intCount += 1
        if intCount == 1:
            RS_Get_AUTHList_by_UserDBName = AUTH_KW_List[0]
            return RS_Get_AUTHList_by_UserDBName
        else:
            RS_Get_AUTHList_by_UserDBName = 'NG:資料不只一筆'
            return RS_Get_AUTHList_by_UserDBName
    else:
        RS_Get_AUTHList_by_UserDBName = 'NG:防火牆關閉'
        return RS_Get_AUTHList_by_UserDBName
    # ***** ***** ***** ***** *****


    ##### LineAUTH ######
def RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineName, strLineUserID, strModUserDBName, strModAUTHItemName, strModYN):
    ##### 資料庫既有的參數 ######
    strCHKUserDBName = 'ECTOR,宜庭,智弘,冠伶,昆霖,玉敏,汶靜,MOMO'
    # TYMEMO   TYFE    TYNEWFE   TYDOOR   TYBT     TYPV      TYDINNER  TYSATEL     TYHRINTERVIEW  TYCAR   TYDORM      TYKW    TYPUSH
    # 備註說明  滅火器  最新滅火器 查詢門禁  查詢體溫  查詢防疫  查詢夜點   查詢業務電話 查詢面試報到    查詢車輛 查詢防疫宿舍 全關鍵字 推播
    strCHKAUTHItemName = '備註說明,滅火器,最新滅火器,查詢門禁,查詢體溫,查詢防疫,查詢夜點,查詢業務電話,查詢面試報到,查詢車輛,查詢防疫宿舍,全關鍵字,推播'
    strCHKYN = 'Y,N'
    # ***** ***** ***** ***** *****

    #取得時間
    datDT = datetime.now()
    strDateTime = datDT.strftime("%Y-%m-%d %H:%M:%S")

    #參數處理
    if len(strModUserDBName.strip()) == 0:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(輸入對象空白)\n\n正確舉例:\n修改權限 ECTOR , 推播 , Y ' + '\n' + \
                    '參數2可用：[ ' + strCHKAUTHItemName + ' ]' + \
                    '參數3可用：[ ' + strCHKYN + ' ]\n'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    if len(strModAUTHItemName.strip()) == 0:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(輸入權限空白)\n\n正確舉例:\n修改權限 ECTOR , 推播 , Y ' + '\n' + \
                    '參數2可用：[ ' + strCHKAUTHItemName + ' ]' + \
                    '參數3可用：[ ' + strCHKYN + ' ]\n'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    if len(strModYN.strip()) == 0:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(輸入YN空白)\n\n正確舉例:\n修改權限 ECTOR , 推播 , Y ' + '\n' + \
                    '參數2可用：[ ' + strCHKAUTHItemName + ' ]' + \
                    '參數3可用：[ ' + strCHKYN + ' ]\n'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    strModUserDBName=strModUserDBName.upper()
    strModAUTHItemName = strModAUTHItemName.upper()
    strModYN = strModYN.upper()

    ##### 檢查輸入資料 ######
    # 取得對象KEY
    if not (strModUserDBName in (strCHKUserDBName.upper())):
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(使用者名稱[ ' + strModUserDBName + ' ]不正確):應為[ ' + strCHKUserDBName + ' ]之一'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    else:
        strFromAUTHItemList = RS_Get_AUTHList_by_UserDBName(strModUserDBName)
        if strFromAUTHItemList[0:2] == 'NG':
            RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(查詢對象權限清單錯誤)'
            exit()

    # 確認開關
    if not (strModYN in (strCHKYN.upper())):
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(設定YN錯誤):應為[ ' + strCHKYN + ' ]之一'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()

    # 確認權限項目
    if not (strModAUTHItemName in (strCHKAUTHItemName.upper()) or strModAUTHItemName in ('修改權限')):
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(權限項目錯誤):應為[ ' + strCHKAUTHItemName + ' ]之一'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    else:
        if strModAUTHItemName == '備註說明':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXMEMO'
                strAUTHTo = 'TYMEMO'
            else:
                strAUTHFrom = 'TYMEMO'
                strAUTHTo = 'TYXMEMO'
        elif strModAUTHItemName == '滅火器':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXFE'
                strAUTHTo = 'TYFE'
            else:
                strAUTHFrom = 'TYFE'
                strAUTHTo = 'TYXFE'
        elif strModAUTHItemName == '最新滅火器':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXNEWFE'
                strAUTHTo = 'TYNEWFE'
            else:
                strAUTHFrom = 'TYNEWFE'
                strAUTHTo = 'TYXNEWFE'
        elif strModAUTHItemName == '查詢體溫':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXBT'
                strAUTHTo = 'TYBT'
            else:
                strAUTHFrom = 'TYBT'
                strAUTHTo = 'TYXBT'
        elif strModAUTHItemName == '查詢防疫':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXPV'
                strAUTHTo = 'TYPV'
            else:
                strAUTHFrom = 'TYPV'
                strAUTHTo = 'TYXPV'
        elif strModAUTHItemName == '查詢夜點':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXDINNER'
                strAUTHTo = 'TYDINNER'
            else:
                strAUTHFrom = 'TYDINNER'
                strAUTHTo = 'TYXDINNER'
        elif strModAUTHItemName == '查詢業務電話':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXSATEL'
                strAUTHTo = 'TYSATEL'
            else:
                strAUTHFrom = 'TYSATEL'
                strAUTHTo = 'TYXSATEL'
        elif strModAUTHItemName == '查詢面試報到':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXHRINTERVIEW'
                strAUTHTo = 'TYHRINTERVIEW'
            else:
                strAUTHFrom = 'TYHRINTERVIEW'
                strAUTHTo = 'TYXHRINTERVIEW'
        elif strModAUTHItemName == '查詢車輛':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXCAR'
                strAUTHTo = 'TYCAR'
            else:
                strAUTHFrom = 'TYCAR'
                strAUTHTo = 'TYXCAR'
        elif strModAUTHItemName == '查詢防疫宿舍':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXDORM'
                strAUTHTo = 'TYDORM'
            else:
                strAUTHFrom = 'TYDORM'
                strAUTHTo = 'TYXDORM'
        elif strModAUTHItemName == '全關鍵字':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXKW'
                strAUTHTo = 'TYKW'
            else:
                strAUTHFrom = 'TYKW'
                strAUTHTo = 'TYXKW'
        elif strModAUTHItemName == '推播':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXPUSH'
                strAUTHTo = 'TYPUSH'
            else:
                strAUTHFrom = 'TYPUSH'
                strAUTHTo = 'TYXPUSH'
        elif strModAUTHItemName == '修改權限':
            if strModYN == 'Y':
                strAUTHFrom = 'TYXPL'
                strAUTHTo = 'TYPL'
            else:
                strAUTHFrom = 'TYPL'
                strAUTHTo = 'TYXPL'
        else:
            RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(特殊狀況):[ 一次只能設定一個權限[ ' + strModAUTHItemName + ' ], 或請擷取畫面並聯絡設計者 ]'
            return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
            exit()
    strToAUTHItemList = strFromAUTHItemList.replace(strAUTHFrom, strAUTHTo)
    # ***** ***** ***** ***** *****

    # 設定權限開關
    if GVstrSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_TYAD_Auth_List]'
        #連線
        ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' UPDATE [TIM_DB].[dbo].[tblAPP_TYAD_Auth_List] ' + \
                    ' SET [AUTH_KW_List] = \'' + strToAUTHItemList + '\', ' + \
                    ' [AUTH_Update] = Convert(nvarchar, \'' + strDateTime + '\', 120), ' + \
                    ' [AUTH_by_UserID] = \'' + strLineUserID + '\', ' + \
                    ' [AUTH_by_LineName] = \'' + strLineName + '\' ' + \
                    ' WHERE [AUTH_MemName] = \'' + strModUserDBName + '\''
        resList = ms.RS_SQL_ExecNonQuery(strSQL)
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = strDateTime + '：\nDB修改OK!' + '\n' + \
                '改[ ' + strModUserDBName + ' ] 的 [ ' + strModAUTHItemName + ' ] 為 [ ' + strModYN + ' ]'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
    else:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG:防火牆關閉'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
    # ***** ***** ***** ***** *****


    ##### LineLOG ######
def RS_Line_LOG_ADD(strLineName, strLineUserID, strKeyInMSG, strLineRpMSG):
    #取得時間
    datDT = datetime.now()
    strDateTime = datDT.strftime("%Y-%m-%d %H:%M:%S")

    #寫入LOG
    if GVstrSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_TYAD_LineLog]'
        #連線
        ms = pymsdb.MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
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
