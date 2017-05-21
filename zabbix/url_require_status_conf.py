#coding:utf8
'''
Created on 2016年8月18日

@author: tianyongkang
'''

import ConfigParser
import sys
import json 

def get_url(section):
    cf = ConfigParser.ConfigParser()
    cf.read('url_require_status.ini')
    v = cf.items(section)[0][1].split(',')

    urls = []
    for i in v:
        urls += [{'{#URLNAME}':i.strip()}]
    print json.dumps({'data':urls},sort_keys=True,indent=7,separators=(',',':'))
    
if __name__ == '__main__':
    get_url(sys.argv[1])