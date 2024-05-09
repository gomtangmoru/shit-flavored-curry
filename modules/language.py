import os.path, json

jsonfile = ['setting.json']
with open(jsonfile[0], 'r') as f:
    j = json.load(f)
    global locale
    locale = j['language']
    with open(os.path.join(os.path.dirname(__file__), f'../locale/{locale}.json'), 'r') as f:
        global langfile;langfile = json.load(f)

#import core_import as ci
class language():
    def CallBackLanguage(self, GetWord):
        ci.load_library(["json"])
    def GivemeLocaleFile(self):
        return langfile
    def WhatismyLocale(self):
        return locale


if __name__ == "__main__":
    print(Exception)

