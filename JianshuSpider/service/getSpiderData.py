# -*- coding: utf-8 -*-
from JianshuSpider.dl.jianshu_topic_feed_data_solve import *

def getSpiderData(pn = 1, rn = 10):
    return getDlSpiderData(pn, rn)

print getSpiderData(1, 10)