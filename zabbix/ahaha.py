#--*-- coding:utf-8 --*--
'''
Created on 2016年7月27日

@author: tianyongkang
'''

from fabric.api import run,env,execute
import os

host = "10.136.50.160"        
env.hosts = ["ubuntu@%s:22" % host,]   
env.password = "fOjTsnIAgi0="   
file_process = "process.txt"    
file_fping = "fping.txt"
 
def fabric_zabbix_proccess_status():
    with file(file_process,'w') as f:    
        f.write(run("sudo zabbix_agentd -t net.tcp.port[%s,10051]" % host)) 
        f.close()

def fabric_zabbix_proccess_start():
    with file(file_process,'r') as f:     
        if int(f.read()[-2]) == 0:       
            os.system('echo "zabbix-server process stoped,process status is 0, now auto start."|mail -s "zabbix server process stoped" tianyongkang@qtonecloud.cn')
            run("sudo /etc/init.d/zabbix-server start")
            

def fabric_zabix_fping_status():
    r = os.popen("/usr/local/bin/fping %s" % host).read()       
    if r.split()[-1] != "alive":         
        os.system('echo "zabbix-server is not alive."|mail -s "zabbix server is not alive" tianyongkang@qtonecloud.cn')
        
def main():
    try:
        execute(fabric_zabbix_proccess_status)
        execute(fabric_zabbix_proccess_start)
    except:
        os.system('echo "fabric_zabbix_proccess_start func have an error!"|mail -s "zabbix server login have an error!" tianyongkang@qtonecloud.cn')
    
    fabric_zabix_fping_status()
      
if __name__ == '__main__':
    main()
    
