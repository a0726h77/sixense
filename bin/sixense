#!/usr/bin/env python
# -*- coding:utf8 -*-

# Author: yan <a0726h77@gmail.com>
# Thanks: yen <yanyan185@gmail.com>
# License: MIT


import time
import os
import sys
import pkgutil
import importlib
import pyperclip
import ConfigParser
from core.Logger import Logger
from thirdparty.Hash_ID_v1_1 import *

#### static variable ####
config_file = "conf/sixense.cfg"
config = ConfigParser.RawConfigParser()
config.read(config_file)
print(config.sections())
# if 'GLOBAL' not in config.sections():
#     config.get('GLOBAL') = {}
#     config['GLOBAL']['DEBUG'] = 1
#     config.write()

logger = Logger('main').__new__()

dictOfNotifiers = {}
dictOfParsers = {}
dictOfTransltors = {}
dictOfDecrypter = {}

#### global variable ####
DEBUG = config.getint('GLOBAL', 'DEBUG')

expectedLang = []

recent_value = pyperclip.paste()  # save current clipboard value


def log(m):
    if DEBUG:
        logger.info(m)


def showMessage(content):
    config_file = "conf/notifier.cfg"
    config = ConfigParser.RawConfigParser()
    config.read(config_file)
    for n, p in dictOfNotifiers.items():
        if config.getint(n, 'enable') != 0:
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


def myDetect(clipboard_content):
    # config = ConfigObj(config_file)

    clipboard_content = clipboard_content.lstrip().rstrip()
    log('########################\n')
    log('Clipboard : %s\n' % clipboard_content)

    # detect string language
    expectedLang = langDetect(clipboard_content)
    clipboard_content = clipboard_content.lstrip().rstrip()

    config_file = "conf/parser.cfg"
    config = ConfigParser.RawConfigParser()
    config.read(config_file)
    log("Parsers :")
    for n, p in dictOfParsers.items():
        if config.getint(n, 'enable') != 0:
            if p.isMatch(clipboard_content):  # 是否符合 parser 規則, 若爲是, 則解析剪貼簿字串
                log('  %s ... match' % p.name)
                gkey = config.get('url', 'gsb_api_key')
                result = p.parse(clipboard_content, gkey)
                if result:
                    showMessage(result)
            else:
                log('  %s ... not match' % p.name)

    log("\n")

    config_file = "conf/translator.cfg"
    config = ConfigParser.RawConfigParser()
    config.read(config_file)
    log("Translators :")
    for n, p in dictOfTranslators.items():
        if config.getint(n, 'enable') != 0:
            if p.isMatch(expectedLang):  # 是否符合 translator 規則, 若爲是, 則解析剪貼簿字串
                log('  %s ... match' % p.name)
                result = p.translate(clipboard_content)
                if result:
                    showMessage(result)
            else:
                log('  %s ... not match' % p.name)

    log("\n")

    config_file = "conf/decrypter.cfg"
    config = ConfigParser.RawConfigParser()
    config.read(config_file)
    hash_expect = expect_hash(clipboard_content)
    if hash_expect:
        log("Possible Hashs:")
        for i in hash_expect:
            if i in dictOfDecrypter:
                log("  [+] %s ... try decrypt" % i)
                vkey = config.get('vt_api_key')
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


def loadModule(module):
    # config = ConfigObj(config_file)

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

        # if module.upper() not in config.keys():
        #     config[module.upper()] = {}
        #     config.write()

        # if m not in config[module.upper()].keys():
        #     config[module.upper()][m] = {}
        #     config[module.upper()][m]['enable'] = 1
        #     config.write()

    return modules


def main():
    global recent_value

    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            myDetect(recent_value)
        time.sleep(0.1)


if __name__ == "__main__":
    dictOfNotifiers = loadModule('notifier')
    dictOfParsers = loadModule('parser')
    dictOfTranslators = loadModule('translator')
    dictOfDecrypter = loadModule('decrypter')

    main()
