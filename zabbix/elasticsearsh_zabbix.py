from elasticsearch import Elasticsearch
import re
import json

es = Elasticsearch([{"host":"10.254.189.115","port":9200}])
r = es.search(index='logstash-weixiao-nginx-accesslog-2016.09.13',body={"query": {"filtered":{"filter":{"range":{"@timestamp":{"ge":'2016-09-14'}}}}}},size=1000,timeout=1000000)
try:
    for i in  r['hits']['hits']:
        v=i['_source']['json']['http_user_agent']
        if re.search('4613',v):
            print v
except KeyError,e:
    print v

i = es.cluster.stats()['status']
   
print json.dumps(i, sort_keys=True, indent=7,separators=(',',':'))