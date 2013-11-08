# coding:utf8

import os
import re

name = 'en2zh'


def isMatch(lang):
    if 'zh' not in lang and 'zh-TW' not in lang:
        return True
    else:
        return False


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
