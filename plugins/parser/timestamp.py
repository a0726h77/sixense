import datetime
from plugins.libs import pretty

name = 'timestamp'


def isMatch(s):
    try:
        datetime.datetime.fromtimestamp(float(s))
        return True
    except:
        return False


def parse(clipboard_content):
    ts = float(clipboard_content)
    _datetime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    _pretty = pretty.date(datetime.datetime.strptime(_datetime, '%Y-%m-%d %H:%M:%S'))

    content = """
Timestamp :
%s

Datetime :
%s

Pretty :
%s
""" % (ts, _datetime, _pretty)

    return content
