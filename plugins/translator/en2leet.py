name = 'en2leet'


def isMatch(lang):
    if 'zh' not in lang and 'zh-TW' not in lang:
        return True
    else:
        return False


def translate(clipboard_content):
    from plugins.libs import leet

    content = """
L33T :
%s
""" % (leet.toLeet(clipboard_content))

    return content
