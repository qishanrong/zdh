#!/bin/env python
#-*-coding:utf-8-*-

import MySQLdb
import sys

host=sys.argv[1]
port=sys.argv[2]
user=sys.argv[3]
passwd=sys.argv[4]
sql=sys.argv[5]


def mysql_exec(sql):
    try:
        conn=MySQLdb.connect(host=host,user=user,passwd=passwd,port=int(port),connect_timeout=5,charset='utf8')
        curs = conn.cursor()
        curs.execute(sql)
        conn.commit()
        curs.close()
        conn.close()
    except Exception,e:
       print "mysql execute: " + str(e)
mysql_exec(sql)
