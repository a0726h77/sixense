#!/usr/bin/env python
# -*- coding:utf8 -*-

# Author: yan <a0726h77@gmail.com>
# Thanks: yen <yanyan185@gmail.com>
# License: MIT


import time
import threading
import os
import sys
import pkgutil
import importlib
from libs import pyperclip
from libs.configobj import ConfigObj
from libs.Hash_ID_v1_1 import *
from libs.Logger import Logger


#### static variable ####
config_file = os.path.join(os.getenv('HOME'), ".sixense.cfg")
config = ConfigObj(config_file)
if 'GLOBAL' not in config.keys():
    config['GLOBAL'] = {}
    config['GLOBAL']['DEBUG'] = 1
    config.write()

logger = Logger('main').__new__()

dictOfNotifiers = {}
dictOfParsers = {}
dictOfTransltors = {}
dictOfDecrypter = {}

#### global variable ####
DEBUG = int(config['GLOBAL']['DEBUG'])

expectedLang = []


def log(m):
    if DEBUG:
        logger.info(m)


def showMessage(content):
    for n, p in dictOfNotifiers.items():
        if int(config['NOTIFIER'][n]['enable']) != 0:
            p.show(content)


def langDetect(s):
    import cld

    langsSeen = set()
    detLangsSeen = set()

    detectedLangName, detectedLangCode, isReliable, textBytesFound, details = cld.detect(s, pickSummaryLanguage=True, removeWeakMatches=False)

    if DEBUG:
        log('CLD :')
        log('  detected: %s' % detectedLangName)
        log('  reliable: %s' % (isReliable != 0))
        log('  textBytes: %s' % textBytesFound)
        log('  details: %s' % str(details))
        for tup in details:
            detLangsSeen.add(tup[0])
        log('  %d langs; %d ever detected' % (len(langsSeen), len(detLangsSeen)))
        log("\n")

    if detectedLangName == 'Unknown':
        return 'Unknown'
    else:
        return [i[1] for i in details]


def is_cliboard_content(content):
    if content and str(content).lstrip().rstrip():
        return True
    else:
        return False


def myDetect(clipboard_content):
    config = ConfigObj(config_file)

    clipboard_content = clipboard_content.lstrip().rstrip()
    log('########################\n')
    log('Clipboard : %s\n' % clipboard_content)

    # detect string language
    expectedLang = langDetect(clipboard_content)
    clipboard_content = clipboard_content.lstrip().rstrip()

    log("Parsers :")
    for n, p in dictOfParsers.items():
        if int(config['PARSER'][n]['enable']) != 0:
            if p.isMatch(clipboard_content):  # 是否符合 parser 規則, 若爲是, 則解析剪貼簿字串
                log('  %s ... match' % p.name)
                gkey = config['PARSER']['url']['gsb_api_key']
                result = p.parse(clipboard_content, gkey)
                if result:
                    showMessage(result)
            else:
                log('  %s ... not match' % p.name)

    log("\n")

    log("Translators :")
    for n, p in dictOfTranslators.items():
        if int(config['TRANSLATOR'][n]['enable']) != 0:
            if p.isMatch(expectedLang):  # 是否符合 translator 規則, 若爲是, 則解析剪貼簿字串
                log('  %s ... match' % p.name)
                result = p.translate(clipboard_content)
                if result:
                    showMessage(result)
            else:
                log('  %s ... not match' % p.name)

    log("\n")

    hash_expect = expect_hash(clipboard_content)
    if hash_expect:
        log("Possible Hashs:")
        for i in hash_expect:
            if i in dictOfDecrypter:
                log("  [+] %s ... try decrypt" % i)
                vkey = config['DECRYPTER']['vt_api_key']
                decrypt_result = dictOfDecrypter[i].decrypt(clipboard_content)
                vt_result = dictOfDecrypter[i].vt_report(clipboard_content, vkey)
                if decrypt_result or vt_result:
                    content = """
String :
%s

Type :
%s

Decrypt :
%s

VirusTotal report :
%s
""" % (clipboard_content, i, decrypt_result, vt_result)
                    showMessage(content)
            else:
                log("  [+] %s ... none" % i)

        log("\n")


class ClipboardWatcher(threading.Thread):
    def __init__(self, predicate, callback, pause=1.):
        super(ClipboardWatcher, self).__init__()
        self._predicate = predicate
        self._callback = callback
        self._pause = pause
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                if self._predicate(recent_value):
                    self._callback(recent_value)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True


def loadModule(module):
    config = ConfigObj(config_file)

    function_string = 'plugins.%s.__file__' % module
    mod_name, func_name = function_string.rsplit('.', 1)
    mod = importlib.import_module(mod_name)
    func = getattr(mod, func_name)
    # result = func()

    MODULE_PATH = os.path.dirname(func)
    MODULE_FILES = [name for _, name, _ in pkgutil.iter_modules([MODULE_PATH])]

    modules = {}
    for m in MODULE_FILES:
        thePluginModuleName = "plugins.%s.%s" % (module, m)
        result = __import__(thePluginModuleName)
        modules[m] = sys.modules[thePluginModuleName]

        if module.upper() not in config.keys():
            config[module.upper()] = {}
            config.write()

        if m not in config[module.upper()].keys():
            config[module.upper()][m] = {}
            config[module.upper()][m]['enable'] = 1
            config.write()

    return modules


if __name__ == "__main__":
    dictOfNotifiers = loadModule('notifier')
    dictOfParsers = loadModule('parser')
    dictOfTranslators = loadModule('translator')
    dictOfDecrypter = loadModule('decrypter')

    # main
    watcher = ClipboardWatcher(is_cliboard_content,
                               myDetect,
                               1.)

    pyperclip.setcb('')  # clear clipboard
    watcher.start()
    while True:
        try:
            # print "Waiting for changed clipboard..."
            time.sleep(5)
        except KeyboardInterrupt:
            watcher.stop()
            break
