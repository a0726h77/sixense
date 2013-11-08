name = 'SHA-1'

def decrypt(clipboard_content):
    import urllib
    import urllib2
    import re

    data = urllib.urlencode({'hash': clipboard_content})
    req = urllib2.Request('http://ez.no-ip.info/', data)
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36')
    result = urllib2.urlopen(req).read()

    match = re.findall("<h3 class='hash'>(.*)</h3>", result)

    if match:
        return match[0]
