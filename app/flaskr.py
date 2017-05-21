#--*-- coding:utf-8 --*--
'''
Created on 2017年1月10日

@author: tianyongkang
'''

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
# 现在通过app.config["VAR_NAME"]，我们可以访问到对应的变量

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
     


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv