#！--*--coding:utf-8--*--
'''
Created on 2017年5月15日

@author: tianyongkang
'''
import urllib2


def gain_token():
    corpid = "wwc881e2187386d708"
    corpsecret = "f8324mOiRab-w2TFvU_KjKnRlaS-u4fiU79IaymPKAI"
    value = urllib2.urlopen("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (corpid,corpsecret))
    return eval(value.read())["access_token"]

