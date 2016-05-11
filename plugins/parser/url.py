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

def google_sb_check(url, apikey):

    from gglsbl import SafeBrowsingList
    sbl = SafeBrowsingList(apikey)

    if sbl.lookup_url(url) is None:
        return 'URL is not in the blacklist.'
    else:
        return '@@ URL is in the blacklist.'

def parse(clipboard_content, apikey):
    content = """
Url :
%s

Url Title :
%s

SafeBrowsing Check:
%s
""" % (clipboard_content, getUrlTitle(clipboard_content), google_sb_check(clipboard_content, apikey))

    return content
