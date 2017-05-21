#--*-- coding:utf8 --*--
'''
Created on 2016年12月21日

@author: tianyongkang
'''

'''
create table test(id int UNSIGNED primary key NOT NULL AUTO_INCREMENT comment "id",
hostname varchar(20) not null DEFAULT "czar" comment "hostname",address varchar(100) not null  
DEFAULT "abc" comment "address") ENGINE=Innodb  DEFAULT CHARSET=utf8mb4 comment "test table";\
insert into test(id,hostname,address) value(7,"czar","acb");\
ALTER TABLE test ADD INDEX idx_host_index(hostname);\
'''

import MySQLdb
from MySQLdb import Error

sql='/*--user=inc;--password=123456;--host=172.16.125.130;--execute=1;--port=3306;*/\
inception_magic_start;\
    select id,hostname from test where hostname="czar";\
inception_magic_commit;'
try:
    conn=MySQLdb.connect(host='172.16.125.130',user='',passwd='',db='',port=6669)
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    num_fields = len(cur.description) 
    field_names = [i[0] for i in cur.description]
    for row in result:
        print row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",
        row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10]
    cur.close()
    conn.close()
except Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])