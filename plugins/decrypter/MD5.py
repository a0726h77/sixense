name = 'MD5'

def decrypt(clipboard_content):
    import urllib
    import re

    result = urllib.urlopen('http://md5.noisette.ch/md5.php?hash=%s' % clipboard_content).read()

    match = re.findall('<string><!\[CDATA\[(.*)\]\]><\/string>', result)

    if match:
        return match[0]
