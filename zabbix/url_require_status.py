#coding :UTF-8
import pycurl
#import StringIO
import sys
#import os


class Callback:
    def __init__(self):
        self.contents=''
    def body_callback(self,buf):
        self.contents=self.contents+buf
def url_require_status(input_url,input_argv):
    t=Callback()
    #gizp_test=file("gzip_test.txt",'w')
    c=pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    
    c.setopt(pycurl.ENCODING,'gzip')
    c.setopt(pycurl.URL,input_url)

    c.perform()
    c.setopt(pycurl.CONNECTTIMEOUT,10)
    http_code=c.getinfo(pycurl.HTTP_CODE)
#    http_conn_time=c.getinfo(pycurl.CONNECT_TIME)
#    http_pre_tran=c.getinfo(pycurl.PRETRANSFER_TIME)
#    http_start_tran=c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time=c.getinfo(pycurl.TOTAL_TIME)
    http_size=c.getinfo(pycurl.SIZE_DOWNLOAD)
    
    
    '''
    if(http_total_time>0.5):
        print "http_code http_size conn_time pre_tran start_tran total_time "
        print "%d %d %f %f %f %f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
    else:
        print ""
        '''
    #print "http_code http_size conn_time pre_tran start_tran total_time "
    #print "%d %d %f %f %f %f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
    if input_argv == 'http_code':
        print http_code
    elif input_argv == 'http_size':
        print http_size
    elif input_argv == 'http_total_time':
        print http_total_time*1000
    
if __name__=='__main__':
    #input_url = sys.argv[1]
    #input_argv = sys.argv[2]
    thistime=url_require_status('http://uww-pro.thinkjoy.com.cn/v2/oauth/token?client_id=ucenter&client_secret=ucenter&grant_type=password&scope=read&username=15206061812&password=4297f44b13955235245b2497399d7a93','http_code')
    