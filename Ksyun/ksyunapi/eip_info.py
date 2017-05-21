#--*-- coding:utf8 --*--
'''
@author: tianyongkang
'''

from ksyun_access import ACCESS_KEY
import json
import datetime
import sys

r = ACCESS_KEY().eip_key().describe_addresses()
#print json.dumps(r,sort_keys=True,indent=4)

d = datetime.datetime.now()
utc_ft = '%Y-%m-%dT%H:%M:%SZ'
starttime = (d - datetime.timedelta(minutes=5)).strftime(utc_ft)
endtime = d.strftime(utc_ft)



m = ACCESS_KEY().monitor_key().get_metric_statistics(InstanceID=sys.argv[1],Namespace="EIP",MetricName=sys.argv[2],StartTime=starttime,EndTime=endtime,Aggregate="Sum",Period="60")
#print json.dumps(m,sort_keys=True,indent=4,separators=(",",":"))
r = m['getMetricStatisticsResult']['datapoints']['member'][2]["sum"]

if r == "null":
    print 0
else:
    print r
