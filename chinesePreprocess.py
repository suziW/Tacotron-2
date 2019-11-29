from xpinyin import Pinyin
import re
from my_utils import stylePrint
# from unidecode import unidecode


specialChars = [
    ('，', ','),
    ('、', ','),
    ('：',':'),
    ('“', "'"),
    ('”', "'"),
    ('。', '.'),
    ('？','?'),
    ('！','!'),
    ('—', '-'),
    ('…','*'),
    ('（', '('),
    ('）', ')'),
    ('0', '零'),
    ('1', '一'),
    ('2', '二'),
    ('3', '三'),
    ('4', '四'),
    ('5', '五'),
    ('6', '六'),
    ('7', '七'),
    ('8', '八'),
    ('9', '九'),
    ]

def chinese2pinyin(chiniese):
    p = Pinyin()
    for regex, replacement in specialChars:
        chiniese = re.sub(regex, replacement, chiniese)
    stylePrint(chiniese, fore='red', back='yellow')

    result = p.get_pinyin(chiniese, splitter=' ', tone_marks='numbers', convert='lower')
    return result

# biaobei preprocess, add special chars to pinyin
def getSpecialCharPositions(chinese):
    chinese = re.sub('#\d', '', chinese)
    replaceList = []
    for char, replace in specialChars:
        patterns = re.finditer(char, chinese)
        for p in patterns:
            replaceList.append((p.span()[0], replace))
    replaceList = sorted(replaceList, key=lambda l: l[0], reverse=False)
    return replaceList

def insertSpecialChar2pinyin(chinese, pinyin):
    inserts = getSpecialCharPositions(chinese)
    # print(inserts)
    pinyin = pinyin.split(' ')
    for pair in inserts:
        pinyin.insert(pair[0], pair[1])
    if '*' in pinyin or '-' in pinyin:
        pinyin = ' '.join(pinyin)
        pinyin = re.sub('\* \*', '**', pinyin)
        pinyin = re.sub('- -', '--', pinyin)
    else:
        pinyin = ' '.join(pinyin)
    return pinyin
    

if __name__ == "__main__":
    chinese = '这不#1因为#1工伤吗#3？上班忙……#2胡乱#1吃早饭#3，加班#1熬夜#3——久坐#1不运动#4……'
    pinyin = 'zhe4 bu4 yin1 wei4 gong1 shang1 ma5 shang4 ban1 mang2 hu2 luan4 chi1 zao3 fan4 jia1 ban1 ao2 ye4 jiu3 zuo4 bu2 yun4 dong4'
    print(insertSpecialChar2pinyin(chinese, pinyin))
    chinese = '1980年，檢調查出，向心夫婦曾多次來台，這次來台——訪友及洽商……'    
    print(chinese2pinyin(chinese))
    print('end')
