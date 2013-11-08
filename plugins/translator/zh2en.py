import os
import re

name = 'zh2en'


def isMatch(lang):
    if 'zh' in lang or 'zh-TW' in lang:
        return True
    else:
        return False


def sdcv(s):
    out = os.popen("sdcv -n '%s'" % s).read()

    content = """
Translate :
%s
""" % (out)

    items_count = re.findall('Found\ (.*)\ items', content)
    if items_count and int(items_count[0]) < 5:
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
