#--*-- coding:UTF-8 -*-
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

class Es_alert:
    #连接es主机
    es = Elasticsearch([{"host":"10.253.2.125","port":9200}])
    def __init__(self,index=''):
        self.index = index
    #获取es index日志内容，默认获取最近十分钟的日志内容，由于ES默认时间是UTC，而且日志是东八区时间，所以需要判断日志时间和es时间。
    def es_get_messages(self,hour_interval=8,minute_interval=10):
        try:
            r = self.es.search(index= self.index, 
              body={"query": 
                   {"filtered": 
                   {"filter":
                   {"range":
                   {"@timestamp":
                   {"gt":datetime.datetime.now() - datetime.timedelta(hours=hour_interval) - datetime.timedelta(minutes=minute_interval) }
                   }}}}}, size=100000)
            
            mesages = []
            for i in r['hits']['hits']: #获取的日志内容格式默认为字典type格式      
                k = i['_source'].keys()
                if "message" in k:
                    mesages.append(i['_source']['message']) 
            #把每条日志记录写入一个list,返回一个list日志列表，yield虽然迭代可以返回所有日志，但是只能被for循环使用一次
            return mesages
            print mesages
        except (UnboundLocalError,TypeError),e:
            print "es_get_messages",e
    #获取es和日志的时间戳，通过判断是否同一个时区，如果不是获取到时间差(东八区和UTC时间相差8个小时)    
    def es_get_timezone(self):
        e = self.es.search(index=self.index,size=1)
        m = e['hits']['hits']
        #print m
        if len(m) > 0 and type(m) == list:
            for i in m:
                if type(i) == dict:
                    if "_source" in i.keys():
                        es_time = i['_source']['@timestamp']      #获取es时间戳 格式为iso8601,2016-05-12T01:56:45.703Z
                        elacticsearch_time = datetime.datetime.strptime(iso8601.parse_date(str(es_time)).strftime("%Y%m%d %H:%M"),"%Y%m%d %H:%M")
                        try:
                            log_time = i['_source']['message']
                            #匹配日志格式，此程序只支持YYYYmmdd-HH:MM:SS,YYYY-mm-dd HH:MM:SS,[YYYYmmdd-HH:MM:SS],[YYYY-mm-dd HH:MM:SS]
                            r = re.search("^(\d+)-(\d+):(\d+):(\d+)|^(\d+)-(\d+)-(\d+).(\d+):(\d+):(\d+)|^\[(\d+)-(\d+):(\d+):(\d+)|^\[(\d+)-(\d+)-(\d+).(\d+):(\d+):(\d+)",log_time)
                            if r is not None:
                                log_date = r.group()
                                try:
                                    d = (datetime.datetime.strptime(str(log_date),"%Y%m%d-%H:%M:%S") - elacticsearch_time).seconds
                                    try:
                                        hour_interval= d / 60 / 60
                                        return hour_interval
                                    except TypeError,e:
                                        print "hour_interval= d / 60 / 60",e                                   
                                except ValueError,e:
                                    try:
                                        d = (datetime.datetime.strptime(str(log_date[1:]), "%Y-%m-%d %H:%M:%S") - elacticsearch_time).seconds
                                        try:
                                            hour_interval = d / 60 /60
                                            return hour_interval
                                        except ValueError,e:
                                            print "hour_interval= d / 60 / 60",e
                                    except ValueError,e:
                                        print self.index,"es_get_timezone() function时间计算错误",e
                        except KeyError,e:
                            print self.index,"es_get_timezone() function:message key missing."
    

    def es_get_shard(self):
        date = datetime.datetime.now().strftime("%Y.%m.%d")
        e = self.es.search_shards("_all")['shards']
        indexs = []
        
        for i in e:
            r = i[0]["index"]
            k = re.search(date,r)
            if k is not None:
                if r not in indexs:
                    indexs.append(r)
        return indexs           


                   
class Es_Alert_filter(Es_alert):
    def __init__(self,index=''):
        Es_alert.__init__(self, index)
        self.index=index
    def es_get_filter(self):
        hour_interval = Es_alert(self.index).es_get_timezone()
        if hour_interval == 8:
            messages =  Es_alert(self.index).es_get_messages(hour_interval,10)
        else:
            messages =  Es_alert(self.index).es_get_messages(8,10)
        
        except_error_filter = []
        except_error_all = []
       
        for i in messages:
            r = re.search('\w+exception\w+',i,re.I)   #不区分大小写，过滤包含exception字符的行
            if r is not None:
                except_error_all.append(r.group())    #所有匹配到exception的字符写入except_error_all列表
                if r.group() not in except_error_filter: #过滤匹配到exception字符的值，去掉重复值写入except_error_filter
                    except_error_filter.append(r.group())
        
        
        
        date = datetime.datetime.now()
        except_list = []
        for i in except_error_filter:
            for m in messages:
                v = re.search(i, m)
                if v is not None:
                    except_list.append((self.index,repr(i),repr(m),date))
        es_mysql.Es_mysql().es_insert_log(except_list)

            


def main():
    print Es_Alert_filter("logstash-qtone-notify-tomcat-log-2016.12.20").es_get_messages()
    #Es_Alert_filter("logstash-zhigaokao--log-2016.05.15").es_get_filter()
   
    #print Es_Alert_filter("logstash-zhigaokao-web-server01-log-2016.05.15").es_get_timezone()
    #p = Es_alert().es_get_shard()
    #print p
    #hour_interval = p.es_get_timezone()
    #print p.es_get_messages(10, hour_interval)

if __name__ == "__main__":
    main()

