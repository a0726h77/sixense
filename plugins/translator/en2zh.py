# coding:utf8

import os
import re

name = 'en2zh'


def isMatch(lang):
    if set(lang) & set(['en', 'af']):  # 白名單
        return True
    elif set(lang) & set(['zh', 'zh-TW']):  # 排除中文語系
        return False
    elif set(lang) & set(['de', 'nl', 'mt', 'cy', 'sl', 'sv', 'sk', 'tr', 'hu', 'lt']):  # 排除歐洲語系
        return False
    else:
        return True


def sdcv(s):
    out = os.popen("sdcv -n -u XDICT英漢辭典 '%s'" % s).read()

    content = """
Translate :
%s
""" % (out)

    items_count = re.findall('Found\ (.*)\ items', content)
    if items_count and int(items_count[0]) < 5:
        return content


def translate(clipboard_content):
    # match = re.findall("([a-zA-Z]+['-]?[a-zA-Z]*)", clipboard_content)
    # result = sdcv(' '.join(match))
    result = sdcv(clipboard_content)

    if result:
        content = """
Your Copy :
%s
%s
""" % (clipboard_content, result)

        return content
