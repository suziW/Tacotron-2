from xpinyin import Pinyin
import re
from my_utils import stylePrint
# from unidecode import unidecode


specialCharsPin = [
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
    ('；', '.'),
    ]

specialCharsHan = [
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
    ('《', ''),
    ('》', ''),
    (' ', ''),
    ]

def chinese2pinyin(chiniese):
    p = Pinyin()
    for regex, replacement in specialCharsHan:
        chiniese = re.sub(regex, replacement, chiniese)
    stylePrint(chiniese, fore='red', back='yellow')

    result = p.get_pinyin(chiniese, splitter=' ', tone_marks='numbers', convert='lower')
    for regex, replacement in specialCharsPin:
        result = re.sub(regex, replacement, result)
    stylePrint(result, fore='red', back='yellow')
    return result

# biaobei preprocess, add special chars to pinyin
def getSpecialCharPositions(chinese):
    chinese = re.sub('#\d', '', chinese)
    replaceList = []
    for char, replace in specialCharsPin:
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
    chinese = '外甥全神贯注的观察中，突然这家伙说了句：“这么点玩意儿怎么够吃。”'
    pinyin = 'wai4 sheng5 quan2 shen2 guan4 zhu4 de5 guan1 cha2 zhong1 tu1 ran2 zhe4 jia1 huo5 shuo1 le5 ju4 zhe4 me5 dian3 wan2 yir4 zen3 me5 gou4 chi1'
    print(insertSpecialChar2pinyin(chinese, pinyin))
    print(chinese2pinyin(chinese))