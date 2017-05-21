#-*- coding:utf-8 -*-
'''
Created on 2016年12月28日

@author: tianyongkang
'''

from  kscore.exceptions import ClientError
from ksyunapi.fetch_monitor_data import KSYUNAPI_MONITOR,KSYUNAPI_KEC
#import json
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

def get_monitor_data():
    m = KSYUNAPI_KEC().list_instance()
    if type(m) == dict:
        if "InstancesSet"  in m.keys():
            v = m["InstancesSet"]
            if len(v) > 0:
                instanceids = []
                instancenames = []
                instancestates = []
                for i in v:
                    instanceid = i["InstanceId"]
                    instanceids.append(instanceid)
                    instanceName = i["InstanceName"]
                    instancenames.append(instanceName)
                    instancestate = i["InstanceState"]["Name"]
                    instancestates.append(instancestate)
                instances = dict(zip(instanceids,instancenames))
                state = dict(zip(instanceids,instancestates))
                
                values = []
                for i in instanceids:
                    if state[i] == "active":
                        try:
                            m = KSYUNAPI_MONITOR(i).list_metrics()["listMetricsResult"]["metrics"]["member"]
                            for key in m:
                                value = (instances[i],i,key["metricName"],KSYUNAPI_MONITOR(i).get_metric_statistics(key["metricName"])["getMetricStatisticsResult"]["datapoints"]["member"][0]["average"],key["unit"])
                                values.append(value)
                        except (ClientError,IndexError):
                            pass
                return values
    
    
#def get_monitor_info():
    #m = ['cpu.utilizition.total', 'system.cpu.load[percpu,avg15]', 'system.cpu.load[percpu,avg1]', 'system.cpu.load[percpu,avg5]', 'system.cpu.util[,idle,avg1]', 'system.cpu.load[all,avg1]', 'system.cpu.load[all,avg5]', 'system.cpu.load[all,avg15]', 'vm.memory.size[available]', 'vm.memory.size[pavailable]', 'vm.memory.size[total]', 'vm.memory.size[used]', 'disk.read.Bps[vda]', 'disk.read.Bps[vdb]', 'disk.read.ops[vda]', 'disk.read.ops[vdb]', 'disk.write.Bps[vda]', 'disk.write.Bps[vdb]', 'disk.write.ops[vda]', 'disk.write.ops[vdb]', 'vfs.fs.size[/,pused]', 'vfs.fs.size[/opt,pused]', 'tcp.count', 'net.if.in[eth0,packets]', 'net.if.in[eth0]', 'net.if.out[eth0,packets]', 'net.if.out[eth0]', 'proc.num[]']
    #u =  ["%", "", "", "", "%", "", "", "", "B", "％", "B", "B", "Bps", "Bps", "Ops", "Ops", "Bps", "Bps", "Ops", "Ops", "%", "%", "", "pps", "Bps", "pps", "Bps", ""]
    
    #return list(zip(m,u))
   
    #m = KSYUNAPI_MONITOR("86dff5ee-ebe9-4da0-a4c5-1ca669839c61").list_metrics()["listMetricsResult"]["metrics"]["member"]
    #print m
    
    #if len(m) > 0:
    #    metricnames = []
    #    units = []
    #    for i in m:
    #        metricnames.append(i["metricName"])
    #        units.append(i["unit"])
    #    d =  map(str,units)
    #    v = json.dumps(d,encoding="UTF-8", ensure_ascii=False)
        #print v
        #print str(metricnames).decode("unicode-escape").encode("utf-8")
    #    values = []
    #    instanceids = []
    #    instanceNames = []
    #    metricnames = ["system.cpu.load[all,avg1]"]
    #    for i in metricnames:
    #        m = KSYUNAPI_MONITOR(instanceid).get_metric_statistics(i)
    #        value = m["getMetricStatisticsResult"]["datapoints"]["member"][-2]["average"]
    #        values.append((value))
    #        instanceids.append(instanceid)
    #        instanceNames.append(instanceName)
    #    v = list(zip(instanceNames,instanceids,metricnames,values,units))
        #return v




            
    