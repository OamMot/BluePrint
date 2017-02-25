# -*- coding: utf-8 -*-

from JianshuSpider.dl.mysql import *
import pymysql
import time

config = {
    'host': '123.59.26.207',
    'port': 3306,
    'user': 'root',
    'password': 'root123',
    'db': 'JianshuSpider',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

connection = connect(config)
# mysql = 'insert into spider_pool(spider_type, user_id, published_at) values (%s, %s, %s)'
# params = ['1', '123', '12345677']
# insert(connection, mysql, params)

# mysql = 'select * from spider_pool'
# result = select(connection, mysql)
# print result

# mysql = 'delete from spider_pool where user_id=%s'
# params = ['123']
# insert(connection, mysql, params)



connection.close()
