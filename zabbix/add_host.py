#!/usr/bin/env python
#--*-- coding:utf-8 --*--
'''
Created on 2016年8月3日

@author: tianyongkang
'''

import urllib2
import json
import socket
import fcntl
import struct

def url_deco(temp):
    def _url_deco(*args, **kwargs):
        try:
            url = 'http://10.136.50.160/api_jsonrpc.php'
            header = {"Content-Type": "application/json"}
            request = urllib2.Request(url, temp(*args))
            for key in header:
                request.add_header(key,header[key])
            result = eval(urllib2.urlopen(request).read())
            return result
        except(urllib2.HTTPError, urllib2.URLError), e:
            return e
    return _url_deco


@url_deco
def zabbix_group_get():
    data = json.dumps(
    {
    "jsonrpc":"2.0",
    "method":"hostgroup.get",
    "params":{
        "output":["groupid","name"],
        "filter":{"groups":""}
    },
    "auth": "17ffc16bbd803845d79da0d13ebb94df",
    "id":1,
    })
    return data





@url_deco
def add_host(groupid=16,ifname="eth0"):
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "127.0.0.1":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ipaddress = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])
    else:
        ipaddress = socket.gethostbyname(socket.gethostname())
    hostname = socket.gethostname()
    data = json.dumps({
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": hostname,
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ipaddress,
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": groupid
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            },
            {
                "templateid": "10104"
             }
        ]
    },
    "auth": "17ffc16bbd803845d79da0d13ebb94df",
    "id": 1
    }
    )
    
    return data



if __name__ == "__main__":
    keys = {}
    for i in  zabbix_group_get()['result']:
        keys[i.values()[1]] = i.values()[0]
    key = raw_input("Please input group name: ")
    for i in keys:
        if key == i:
            print add_host(keys[i])
        elif key == '':
            print add_host()
            

