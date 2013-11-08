name = 'url_but_not_bitly'


def isMatch(url):
    if url.startswith("http://") or url.startswith("https://") and not "bit.ly" in url:
        return True
    return False


def getUrlTitle(s):
    import urllib
    import BeautifulSoup

    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s))

    return soup.title.string


def parse(clipboard_content):
    content = """
Url :
%s

Url Title :
%s
""" % (clipboard_content, getUrlTitle(clipboard_content))

    return content
