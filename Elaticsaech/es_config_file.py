#-*- coding: UTF-8 -*-
import ConfigParser
import datetime 
import es_get_data
import re

class Es_index:
    def es_get_index(self):
        index_list = es_get_data.Es_alert().es_get_shard()
        conf = ConfigParser.ConfigParser()
        conf.read("es.conf")

        #获取指定的section，指定的option的值
        index_name = conf.get("index","name")
    
        indexs = []
        for i in index_list:
            try:
                if re.search(index_name,i) is not None:
                    indexs.append(i)
            except AttributeError, e:
                print e
        return indexs


#print es_get_data.Es_alert('logstash-zhigaokao-web-server01-log-2016.05.12').es_get_messages(3,8)
#print Es_index().es_get_index()
#print conf.sections()



