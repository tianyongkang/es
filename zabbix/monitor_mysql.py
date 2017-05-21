#!/usr/bin/python
#coding:utf-8
'''
Created on 2016年8月24日

@author: tianyongkang
'''

import MySQLdb
import sys
import os
import json

def monitor_host():
    host = '10.136.50.160'
    user = 'root'
    passwd = 'thinkjoy#123'
    port = 3306
    db = 'monitor_mysql'

    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,port=port)
    cur = conn.cursor()
    cur.execute('select * from info;')
    r = cur.fetchall()
    return r
    cur.close()
    conn.close()

def mysql_status(input_arg, input_args=0, *args, **kwargs):
    p = monitor_host()
    keys = {}
    for i in p:
        keys[i[2]] = [i[1],i[3],i[4]]
    if input_arg == 'discovery':
        hosts = []
        for k in keys:
            hosts += [{'{#DBNAME}':k}]
        print json.dumps({'data':hosts},sort_keys=True,indent=7,separators=(',',':'))

    else:
        for k in keys:
            mysql_alive = os.popen('zabbix_agentd -t net.tcp.port[%s,3306]' % k).read().strip()[-2]
            if k == input_arg and int(mysql_alive) == 1:
                conn = MySQLdb.connect(host=k,user=keys[k][1],passwd=keys[k][2])
                cur = conn.cursor()
                cur.execute('show global status;')
                r = cur.fetchall()
                cur.close()
                conn.close()
                for i in r:
                    if i[0] == input_args:
                        print i[1]

 

if sys.argv[1] == 'discovery':
    mysql_status(sys.argv[1])
else:
    mysql_status(sys.argv[1],sys.argv[2])