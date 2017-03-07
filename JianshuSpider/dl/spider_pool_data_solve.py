# -*- coding: utf-8 -*-
from JianshuSpider.dl.mysql import *

def getDlSpiderPool(pn = 1, rn = 10):
    conn = connect()
    sql = 'select * from spider_pool limit %s, %s'
    _from = (pn - 1) * rn
    _to = pn * rn - 1
    params = [_from, _to]
    arrOutput = select(conn, sql, params)
    return arrOutput