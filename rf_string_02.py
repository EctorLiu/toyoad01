    ##### INDEX ######
# def RS_LEFT_String_StrNum(strTemp, intNum): 取字串左邊幾個字 => (ABCDE, 2)取(AB)
# def RS_RIGHT_String_StrNum(strTemp, intNum): 取字串右邊幾個字 => (ABCDE, 2)取(DE)
# def RS_RIGHT_String_NotLeftStrNum(strTemp, intNum): 不取字串左邊幾個字 => (ABCDE, 2)取(CDE)
# def RS_MID_String_Start_StrNum(strTemp, intStart, intNum): 取字串中間開始幾個字 => (ABCDE, 2, 3)取(BCD)
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

def RS_LEFT_String_StrNum(strTemp, intNum):
    return strTemp[:intNum]

def RS_RIGHT_String_StrNum(strTemp, intNum):
    return strTemp[-intNum:]

def RS_RIGHT_String_NotLeftStrNum(strTemp, intNum):
    if len(strTemp) == intNum:
        return ''
    else:
        return strTemp[-(len(strTemp)-intNum):]

def RS_MID_String_Start_StrNum(strTemp, intStart, intNum):
    return strTemp[intStart:intStart+intNum]
    # ***** ***** ***** ***** *****
