    ##### 字串處理 ######
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
