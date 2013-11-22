# coding:utf8

import os
import re
name = 'fr2cn'


def isMatch(lang):
    if set(lang) & set(['en', 'af', 'fr', 'ga', 'sq', 'it', 'nb', 'ht', 'ms', 'fi', 'ca', 'id', 'is', 'nl', 'ro', 'hil', 'tr', 'pt', 'sv', 'sk', 'hu', 'cy', 'da']):
        return True
    else:
        return False


def sdcv(s):
    out = os.popen("sdcv -n -u 我爱法语-法汉词典 \"%s\"" % s).read()
    items_count = re.findall('Found\ (.*)\ items', out)

    if items_count and int(items_count[0]) <= 3:
        content = """
Translate :
%s
""" % (out)

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
