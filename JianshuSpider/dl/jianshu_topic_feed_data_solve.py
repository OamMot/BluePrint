# -*- coding: utf-8 -*-
from JianshuSpider.dl.mysql import *


def insertDlSpiderData(data = []):
    conn = connect()
    boolRepeat = 0

    for i in data:
        topic_identify = i['topic_identify']
        mysql = 'select * from jianshu_topic_feed where topic_identify=%s'
        params = [topic_identify]
        selectInfo = select(conn, mysql, params)
        if len(selectInfo) > 0:
            boolRepeat = 1
            continue;
        mysql = 'insert into jianshu_topic_feed(user_id, topic_identify, title, summary, published_at, inserted_at, pool_id) ' \
                                        'values(%s, %s, %s, %s, %s, %s, %s)'
        arrInput = [1, i['topic_identify'], i['title'], i['summary'], i['published_at'], i['inserted_at'], i['pool_id']]
        insert(conn, mysql, arrInput)

    conn.close()
    return boolRepeat

def getDlSpiderData(pn = 1, rn = 10):
    conn = connect()

    _from = (pn - 1) * rn
    _to = pn * rn - 1
    mysql = 'select * from jianshu_topic_feed limit %s,%s'
    params = [_from, _to]
    arrOutput = select(conn, mysql, params)
    conn.close()
    return arrOutput
