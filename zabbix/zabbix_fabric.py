#--*-- coding:utf-8 --*--
'''
Created on 2016年7月27日

@author: tianyongkang
'''

from fabric.api import run,env,execute,local
import os

host = "10.136.50.160"        
env.hosts = ["ubuntu@%s:22" % host,]   #ssh连接方式，模式22端口的话，可以不用写:22,这是个list。
env.password = "fOjTsnIAgi0="   #账号密码
file_process = "process.txt"    
file_fping = "fping.txt"
 
def fabric_zabbix_proccess_status():
    with file(file_process,'w') as f:    #把结果输出到文件里面
        f.write(run("sudo zabbix_agentd -t net.tcp.port[%s,10051]" % host)) #远程执行命令，获取当前zabbix-server进程状态
        f.close()

def fabric_zabbix_proccess_start():
    with file(file_process,'r') as f:     #读取上一步的文件输出内容
        if int(f.read()[-2]) == 0:        #判断获取的数据是否为1，1的话服务正常，0为进程关闭
            os.system('echo "zabbix-server process stoped,process status is 0, now auto start."|mail -s "zabbix server process stoped" tianyongkang@qtonecloud.cn')
            run("sudo /etc/init.d/zabbix-server start") #如果获取的值是0，就执行zabbix-server启动命令
            

def fabric_zabix_fping_status():
    r = os.popen("/usr/local/bin/fping %s" % host).read()       #fping zabbix-server主机
    if r.split()[-1] != "alive":          #如果ping不通发送邮件
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
    
