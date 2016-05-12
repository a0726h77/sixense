name = 'SHA-256'

def decrypt(clipboard_content):
    return 0

def vt_report(clipboard_content, apikey):
    import simplejson
    import urllib
    import urllib2
    # url = "https://www.virustotal.com/vtapi/v2/comments/put"
    # url = "https://www.virustotal.com/vtapi/v2/file/rescan"
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    parameters = {"resource": clipboard_content,
                  "comment": "How to disinfect you from this file... #disinfect #zbot",
                  "apikey": apikey}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    # print json.positives
    response_dict = simplejson.loads(json)
    return response_dict.get("positives", {})
