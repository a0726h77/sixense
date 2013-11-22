# coding:utf8

import os
import re
name = 'de2zh'


def isMatch(lang):
    if set(lang) & set(['en', 'de', 'nl', 'mt', 'cy', 'sl', 'sv', 'sk', 'fr', 'tr', 'hu', 'lt']):
        return True
    else:
        return False


def sdcv(s):
    out = os.popen("sdcv -n -u Fundset德汉词典 '%s'" % s).read()
    items_count = re.findall('Found\ (.*)\ items', out)

    if items_count and int(items_count[0]) != 1:
        out = os.popen("sdcv -n -u 新德汉词典 '%s'" % s).read()
        items_count = re.findall('Found\ (.*)\ items', out)

    if items_count and int(items_count[0]) == 1:
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
