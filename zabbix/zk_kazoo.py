#!--*--coding:utf-8 --*--
'''
Created on 2016年7月26日

@author: tianyongkang
'''

from kazoo.client import KazooClient

zk = KazooClient('host=10.136.3.214:2181')
zk.start(timeout=20)
r = zk.command(cmd="conf")
