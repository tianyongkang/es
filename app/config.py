#--*-- coding:utf-8 --*--
'''
Created on 2017年1月11日

@author: tianyongkang
'''

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flaskext.mysql import MySQL


DEBUG = True # 启动Flask的Debug模式
BCRYPT_LEVEL = 13 # 配置Flask-Bcrypt拓展
MAIL_FROM_EMAIL = "robert@example.com" # 设置邮件来源


MYSQL_DATABASE_HOST = "localhost"
MYSQL_DATABASE_PORT = 3306
MYSQL_DATABASE_USER = "root"
MYSQL_DATABASE_PASSWORD = "1234.com"
MYSQL_DATABASE_DB = "ksyunapi"
#MYSQL_DATABASE_CHARSET = "uft8"

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def get_connect():
    mysql = MySQL(app)
    mysql.init_app(app)
    cursor = mysql.connect().cursor()
    cursor.execute("show databases;")
    print cursor.fetchall()

get_connect()

@app.route('/')
def show_entries():
    print get_connect()

if __name__ == '__main__':
    app.run()


