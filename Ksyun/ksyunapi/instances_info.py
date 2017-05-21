#--*-- coding:utf8 --*--
'''
Created on 2016年12月28日

@author: tianyongkang
'''
from ksyunapi.fetch_monitor_data import KSYUNAPI_KEC


def get_instances():
    m = KSYUNAPI_KEC().list_instance()
    if type(m) == dict:
        if "InstancesSet"  in m.keys():
            v = m["InstancesSet"]
            if len(v) > 0:
                instanceinfo = []
                for i in v:
                    instanceid = i["InstanceId"]
                    instanceName = i["InstanceName"]
                    instancestate = i["InstanceState"]["Name"]
                    macaddress = i["NetworkInterfaceSet"][0]["MacAddress"]
                    privateipaddress = i["NetworkInterfaceSet"][0]["PrivateIpAddress"]
                    datadiskgb = i["InstanceConfigure"]["DataDiskGb"]
                    dataaisktype = i["InstanceConfigure"]["DataDiskType"]
                    memorygb = i["InstanceConfigure"]["MemoryGb"]
                    vcpu = i["InstanceConfigure"]["VCPU"]
                    
                    value = (instanceid,instanceName,instancestate,macaddress,privateipaddress,datadiskgb,dataaisktype,memorygb,vcpu)
                    instanceinfo.append(value)
                return instanceinfo



