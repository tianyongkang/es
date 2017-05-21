#/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年12月28日

@author: tianyongkang
'''

import MySQLdb
from ksyunapi.instances_info import get_instances
from ksyunapi.monitor_info import get_monitor_data
import json
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def mysql_keyun(func):
    def mysqlconn():
        conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="1234.com",db="ksyunapi",port=3306,charset='utf8')
        cur = conn.cursor()
        cur.execute(func())
        conn.commit()
        cur.close()
        conn.close()
    return mysqlconn
        

@mysql_keyun
def my_instances_info():
    d = []
    for i in get_instances():
        d.append(tuple(map(str,i)))
    v = json.dumps(d,encoding="UTF-8", ensure_ascii=False)
    value =  re.sub(r"\]",")",re.sub(r"\[","(",str(v[1:-1])))
    
    data = "insert into instance_info(instanceid,instanceName,instancestate,macaddress,privateipaddress,datadiskgb,dataaisktype,memorygb,vcpu) values%s" % value
    return data


@mysql_keyun
def my_monitor_data():
    d = []
    for i in get_monitor_data():
        d.append(tuple(map(str,i)))
    v = json.dumps(d,encoding="UTF-8", ensure_ascii=False)
    value =  re.sub(r"\]",")",re.sub(r"\[","(",str(v[1:-1])))
    data = "insert into monitor_info(instancename,instanceid,metricname,value,unit) values%s" % value
    return data

my_monitor_data()


