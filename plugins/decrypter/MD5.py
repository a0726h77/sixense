name = 'MD5'

def decrypt(clipboard_content):
    import urllib
    import re
    import json

    # result = urllib.urlopen('http://md5.noisette.ch/md5.php?hash=%s' % clipboard_content).read()
    # result = urllib.urlopen('http://hashes.org/api.php?do=check&hash1=%s' % clipboard_content).read()

    # match = re.findall('<string><!\[CDATA\[(.*)\]\]><\/string>', result)
    #
    # if match:
    #     return match[0]

    type   = "crack"
    apikey = "736b45c7150d61d15604e132"
    phrase = clipboard_content

    result = urllib.urlopen('http://api.md5crack.com/%s/%s/%s' % (type, apikey, phrase)).read()

    if(json.loads(result)['parsed']):
        return json.loads(result)['parsed']
