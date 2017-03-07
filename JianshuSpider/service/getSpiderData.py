# -*- coding: utf-8 -*-
from JianshuSpider.dl.jianshu_topic_feed_data_solve import *
from JianshuSpider.dl.spider_pool_data_solve import *

def getSpiderData(pn = 1, rn = 10):
    return getDlSpiderData(pn, rn)

def getSpiderPool(pn = 1, rn = 10):
    return getDlSpiderPool(pn, rn);
