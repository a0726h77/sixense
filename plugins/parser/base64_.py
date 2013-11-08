import base64
import binascii
import re

name = 'base64'


def isMatch(s):
    valid = re.match('^[\w+/=]+$', s)
    if valid:
        try:
            base64.decodestring(s).decode('utf8')
            return True
        except:
            return False
    else:
        return False


def parse(s):
    s_decoded = base64.b64decode(s)
    content = """
Your Copy :
%s

Decode :
%s
""" % (s, s_decoded)

    if '\n' not in s_decoded:
        return content
    else:
        return ''
