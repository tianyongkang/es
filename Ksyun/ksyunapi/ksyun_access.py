#--*-- coding:utf8 --*--
'''
Created on 2016年12月27日

@author: tianyongkang
'''
from kscore.session import get_session
from cinderclient.client import Client


class ACCESS_KEY:
    ACCESS_KEY_ID = "AKLTSjl1yfHFSzK94IgwQTLhXA"
    SECRET_ACCESS_KEY = "OATQfvpruVBFrIyL2A1BTSZ86OLZlQ3p5PqCo02yGjhHDYkY6Dfq+dsCUur4NQ7vMg=="
    def monitor_key(self,module="monitor",region="cn-beijing-6",):
        client = get_session().create_client(module,region,ks_access_key_id=self.ACCESS_KEY_ID, ks_secret_access_key=self.SECRET_ACCESS_KEY,use_ssl=True)
        return client
    
    
    def eip_key(self,module="eip",region="cn-beijing-6"):
        client = get_session().create_client(module,region,ks_access_key_id=self.ACCESS_KEY_ID, ks_secret_access_key=self.SECRET_ACCESS_KEY,use_ssl=False)
        return client


