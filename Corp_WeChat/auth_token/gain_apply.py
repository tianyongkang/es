#/usr/bin/python
#!-*-coding:utf-8 -*-
'''
Created on 2017年5月15日

@author: tianyongkang
'''
from gain_access_token import gain_token
import urllib2
import json


def gain_apply():
    agentid = 1000002
    access_token =  gain_token()
    value = urllib2.urlopen("https://qyapi.weixin.qq.com/cgi-bin/agent/get?access_token=%s&agentid=%s" % (access_token,agentid))
    return value

print json.dumps(eval(gain_apply().read()),sort_keys=True,indent=4,separators=(",",":"),ensure_ascii=False)

