#--*--coding: utf8 --*--
'''
Created on 2016年12月26日

@author: tianyongkang
'''
from ksyunapi.ksyun_access import ACCESS_KEY
import datetime


class KSYUNAPI_MONITOR:
    def __init__(self,inst="null"):
        self.inst = inst
        self.client = ACCESS_KEY().monitor_key()
    
    def list_metrics(self):
        m=self.client.list_metrics(InstanceID=self.inst,Namespace="kec",PageIndex="1",PageSize="1000")
        return m
    
    def get_metric_statistics(self,metricname):
        d = datetime.datetime.now()
        utc_ft = '%Y-%m-%dT%H:%M:%SZ'
        starttime = (d - datetime.timedelta(minutes=10)).strftime(utc_ft)
        endtime = d.strftime(utc_ft)
        m=self.client.get_metric_statistics(InstanceID=self.inst,Namespace="kec",MetricName=metricname,StartTime=starttime,EndTime=endtime,Period="300",Aggregate="Average,Max,Min,Count,Sum")
        return m

class KSYUNAPI_KEC:
    def __init__(self):
        self.client = ACCESS_KEY().monitor_key("kec")
        
    def list_instance(self):
        m = self.client.describe_instances(MaxResults=1000)
        return m
    
#print KSYUNAPI_KEC().list_instance()
#print KSYUNAPI_MONITOR("86dff5ee-ebe9-4da0-a4c5-1ca669839c61").get_metric_statistics("vm.memory.size[available]")

