#--*-- coding:utf8 --*--
'''
Created on 2016年12月20日

@author: tianyongkang
'''

from elasticsearch import Elasticsearch
#import requests
#import json
import datetime
import iso8601
#import time
#import sys 
import re
#import os
import es_mysql
import json

class Es_alert:
    #连接es主机
    es = Elasticsearch([{"host":"10.253.2.125","port":9200}])
    def __init__(self,index=''):
        self.index = index
    #获取es index日志内容，默认获取最近十分钟的日志内容，由于ES默认时间是UTC，而且日志是东八区时间，所以需要判断日志时间和es时间。
    def es_get_messages(self,hour_interval=8,minute_interval=60):
        try:
            r = self.es.search(index= self.index, 
              body={"query": 
                   {"filtered": 
                   {"filter":
                   {"range":
                   {"@timestamp":
                   {"gt":datetime.datetime.now() - datetime.timedelta(hours=hour_interval) - datetime.timedelta(minutes=minute_interval) }
                   }}}}}, size=1)
            
            print json.dumps(r,sort_keys=True,indent=4,separators=(",",":"))
        except (UnboundLocalError,TypeError),e:
            print "es_get_messages",e
            
Es_alert('logstash-weixiao-nginx-accesslog-2016.12.23').es_get_messages()

