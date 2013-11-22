# coding:utf8

import os
import re
name = 'ja2cn'


def isMatch(lang):
    if set(lang) & set(['ja', 'zh']):
        return True
    else:
        return False


def sdcv(s):
    content = "\nTranslate :"

    # 第一部分翻譯
    out = os.popen("sdcv -n -u 日中简明专业词典 '%s'" % s).read()
    items_count = re.findall('Found\ (.*)\ items', out)

    if items_count and int(items_count[0]) == 1:
        content = content + """
%s""" % (out)

    # 第二部分翻譯
    out = os.popen("sdcv -n -u DrEye日汉词典 '%s'" % s).read()
    items_count = re.findall('Found\ (.*)\ items', out)
    if items_count and (int(items_count[0]) == 1):
        content = content + out

    if (not items_count) or (int(items_count[0]) != 1):
        out = os.popen("sdcv -n -u jmdict-ja-en '%s'" % s).read()
        items_count = re.findall('Found\ (.*)\ items', out)
        if items_count and (int(items_count[0]) == 1):
            content = content + out

    if content != "\nTranslate :":
        return content


def translate(clipboard_content):
    result = sdcv(clipboard_content)

    if result:
        content = """
Your Copy :
%s
%s
""" % (clipboard_content, result)

        return content
