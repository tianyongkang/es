#!/usr/bin/python
#--*-- coding:gbk --*--

import json
import urllib2
import re
import sys
from urllib2 import Request, urlopen, URLError, HTTPError
from zabbix_auth import zabbix_auth
auth = zabbix_auth()



reload(sys)
#sys.setdefaultencoding('utf8')

def url_deco(temp):
    def _url_deco(*args, **kwargs):
        try:
            #url = 'http://10.10.68.11/zabbix/api_jsonrpc.php'
            #url = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
            url = 'http://172.31.0.5/zabbix/api_jsonrpc.php'
            header = {"Content-Type": "application/json"}
            request = urllib2.Request(url, temp(*args))
            for key in header:
                request.add_header(key,header[key])
            #print urllib2.urlopen(request).read()
            result = eval(urllib2.urlopen(request).read())
	        return result
	    except(urllib2.HTTPError, urllib2.URLError), e:
	       return e
    return _url_deco


def zabbix_host_create():
    hi = {}
    hostnames = []
    ipaddresses = []
    groupids = []
    templateids = []
    proxyids = []
    
    vlist = ["HOSTIP", "GROUP", "TEMPLATE","PROXY"]
    with open("zabbix_create.conf", "r") as v:
        for i in v.readlines():
            if re.search("^\w", i) is not None:
                k = i.strip()
		
                for vl in vlist: 		
                    if re.search(vl, k) is not None:
                        h = k.split("=")[1].strip()
                        d = eval(h)
		        if vl == "HOSTIP":
			    hi.update(d)
			if d != 0:
			    for k, v in d.items():
				if vl == "HOSTIP":
				    hostnames.append(k)
                                    ipaddresses.append(v)
				elif vl == "GROUP":
				    groupids.append(v)
				elif vl == "TEMPLATE":
				    templateids.append(v)
				elif vl == "PROXY":
				    proxyids.append(v)
				else:
				    print "NO define host or ip or group or template!"
    templates = []
    groups = []
    for i in range(0,len(templateids)):
        templates.append({"templateid": templateids[i]})
    for i in range(0,len(groupids)):
	groups.append({"groupid": groupids[i]})

    if len(proxyids) == 1:
	proxyid = proxyids[0]
    else:
	proxyid = 0

    for hostname, ipaddress in hi.items():
        data = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": hostname,
  	    "proxyid": proxyid,
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
    		    "groupid": "8"
    		}
            ],
            "templates": [
    		{
    		    "templateid": "10001"
    		}
            ]
        },
        "auth": auth,
        "id": 1
        }
	
	data["params"]["templates"] = templates
	data["params"]["groups"] = groups
	url = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
        header = {"Content-Type": "application/json"}
        request = urllib2.Request(url, json.dumps(data))
        for key in header:
            request.add_header(key,header[key])
        print urllib2.urlopen(request).read()   
	#print proxyid

@url_deco
def zabbix_proxy_update(proxyid, hostid):
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "proxy.update",
    "params": {
        "proxyid": proxyid,
        "hosts": [
            hostid
        ]
    },
    "auth": auth,
    "id": 1
    }
    )
    return data

@url_deco
def zabbix_host_get():
    data = json.dumps(
    {
        "jsonrpc":"2.0",
        "method":"host.get",
        "params":{
            "output":["hostid", "name", "host"],
            "filter":{"host":""}
    },
        "auth": auth,
    "id":1,
    })
    return data	

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
    "auth": auth,
    "id":1,
    })    
    return data

@url_deco
def zabbix_get_host_data(name):
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
                name
            ]
        }
    },
    "auth": auth,
    "id": 2
    }
    )
    return data

@url_deco	
def zabbix_host_update(hostid, groupid):
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "host.update",
    "params": {
        "hostid": hostid,
        "groups": [
	    { "groupid": groupid }
    ]
    },
    "auth": auth,
    "id": 1
    }
    )
    return data

@url_deco
def zabbix_template_get():
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": ["templateid", "host"],
        "filter": 
            "templateids"
    },
    "auth": auth,
    "id": 1
    }
    )
    return data

@url_deco
def zabbix_trigger_get():
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "filter": {
            "host": ["Zabbix server"]
        },
        "output": "extend"
    },
    "auth": auth,
    "id": 2
    }
    )
    return data


@url_deco
def zabbix_proxy_get():
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "proxy.get",
    "params": {
        "output": ["host","proxyid"],
        "selectInterfaces": "extend"
    },
    "auth": auth,
    "id": 1
    }
    )
    return data

@url_deco
def zabbix_history_get():
    data = json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "history.get",
    "params": {
        "output": "extend",
        "history": 0,
#        "itemids": "23296",
	"hostids": "10180",
        "sortfield": "clock",
        "sortorder": "DESC",
        "limit": 1000
    },
    "auth": auth,
    "id": 1
    }
    )
    return data

@url_deco
def zabbix_item_get():
    data= json.dumps(
    {
    "jsonrpc": "2.0",
    "method": "item.get",
    "templateids": 0,
    "templated": "Template OS Linux",
    #"hostids": "10180",
    "params": {
        #"output": ["itemid","key_","name","templateid"],
        "search": {
            #"key_": "system"
        },
        "sortfield": "name"
    },
    "auth": auth,
    "id": 1
    }
    )
    return data
	
def result_deco(output):
    def _result_deco(*args, **kwargs):
        r = output()
	try:
	    for i in r["result"]:
		keys = {}
		for key in i:
                    keys[key]=i[key].decode('unicode-escape') 
	        return json.dumps(keys,encoding='utf-8',ensure_ascii=False)
	        #print json.dumps(v, sort_keys=True, indent=4, separators=(',',','))
        except (KeyError,TypeError), e:
	    print "Please python %s -p" % sys.argv[0]    
    return _result_deco



#@result_deco
def main():
    if sys.argv[1] == '--host-list':
        return zabbix_host_get()        
    elif sys.argv[1] == '--group-list':
        return zabbix_group_get()
    elif sys.argv[1] == '--template-list':
	print json.dumps(zabbix_template_get(),sort_keys=True,indent=4,separators=(',',':'))
    elif sys.argv[1] == '--trigger-list':
	return zabbix_trigger_get()
    elif sys.argv[1] == '--proxy-list':
	return zabbix_proxy_get()
    elif sys.argv[1] == '--proxy-update':
	return zabbix_proxy_update()
    elif sys.argv[1] == '--history-list':
	return zabbix_history_get()
    elif sys.argv[1] == '--item-list':
	return zabbix_item_get()
    elif sys.argv[1] == '--host-group-update':
	r = zabbix_host_get(sys.argv[2])
	hs = zabbix_group_get()
	for h in hs:
	    if sys.argv[3] == hs[h]:
	        for i in r:
	            return zabbix_host_update(i, h)
    elif sys.argv[1] == '-p':
	print "sys.argv[1] parameter: --host-create, --host-list,--group-list,--template-list,--trigger-list"
    else:
        print "sys.argv[1] parameter: --host-create, --host-list,--group-list,--template-list,--trigger-list"

if __name__ == '__main__':
    main()

#    try:
#        if sys.argv[1] == '--host-create':
#	    zabbix_host_create()
#        else:
#            main()
#    except IndexError, e:
#	print "sys.argv[1] parameter: --host-create, --host-list,--group-list,--template-list,--trigger-list"
