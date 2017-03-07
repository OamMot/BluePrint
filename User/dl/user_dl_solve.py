# -*- coding: utf-8 -*-
from JianshuSpider.dl.mysql import *
import time

def dlLogin(user_name = '', avatar = '', discription = ''):
    conn = connect()
    # sql = 'insert '

def dlFollowSomething(user_id, type, identify, follow_num):
    conn = connect()
    timestamp = time.time()
    sql = 'insert into spider_pool (identify, spider_type, published_at, follow_num) Values' \
          '(%s, %s, %s, %s)'
    params = [identify, 0, timestamp, follow_num]
    insert(conn, sql, params)
    conn.close()

def dlSelectSomething(user_id, type, identify):
    conn = connect()
    sql = 'select * from spider_pool where identify=%s'
    print sql, '-------------------'
    params = [identify]
    print params, '--------------------'
    arrOutput = select(conn, sql, params)
    conn.close()
    return arrOutput

def dlInsertUserSpiderPool(user_id, pool_id, published_at):
    conn = connect()
    sql = 'insert into user_spider_pool (user_id, pool_id, published_at) Values' \
          '(%s, %s, %s)'
    params = [user_id, pool_id, published_at]
    arrOutput = insert(conn, sql, params)
    conn.close()
    return arrOutput

def dlUpdateUserSpiderPool(user_id, pool_id, published_at, follow_num):
    conn = connect()
    sql = 'insert into user_spider_pool (user_id, pool_id, published_at, follow_num) Values' \
          '(%s, %s, %s, %s)'
    params = [user_id, pool_id, published_at, follow_num]
    arrOutput = insert(conn, sql, params)
    conn.close()
    return arrOutput