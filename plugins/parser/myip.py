name = 'myip'


def isMatch(s):
    if 'my' in s.lower() and 'ip' in s.lower():
        return True
    else:
        return False


def parse(clipboard_content):
    import urllib
    ip = urllib.urlopen('http://icanhazip.com').read()

    content = """
My IP :
%s
""" % ip

    return content
