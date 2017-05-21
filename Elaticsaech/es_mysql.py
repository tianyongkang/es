#-*- coding:utf-8 -*-

import MySQLdb
import datetime

class Es_mysql:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = MySQLdb.connect(host="localhost",user="root",passwd="1234.com")
    def __init__(self):
        pass
        
    def es_create_db(self):
        try:
            cur = self.conn.cursor()
            cur.execute("drop database if exists elaticsearch;")
            cur.execute("CREATE  DATABASE  elaticsearch  CHARACTER SET  utf8  COLLATE utf8_general_ci")
            self.conn.select_db("elaticsearch")
            cur.execute("create table except(id int primary key auto_increment,index_name varchar(100) not null,except_type varchar(100),except_log longtext,date_time datetime);")
            cur.execute("desc except")
            r = cur.fetchall()
            print r
            self.conn.commit()
            cur.close()
        except MySQLdb.Error,e:
            print e
        finally:
            self.conn.close()
    
    def es_insert_log(self,*args,**kwargs):
        try:
            cur = self.conn.cursor()
            self.conn.select_db("elaticsearch")
            sql = "insert into except(index_name,except_type,except_log,date_time) values(%s,%s,%s,%s);"
            cur.executemany(sql,*args)
            self.conn.commit()
            cur.close()
        except (MySQLdb.Error,MySQLdb.ProgrammingError),e:
            print e
        finally:
            #pass 
            self.conn.close()
        

#print es_get_data.Es_Alert_filter("logstash-ucenter-tomcat-log-2016.05.14").es_get_filter()
