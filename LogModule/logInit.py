# -*- coding: utf-8 -*-
import logging
import time
import os

def initLog():
    YMDH = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
    dic = '../logs'
    if (os.path.exists(dic) == False):
        os.makedirs(dic)

    filename = '../logs/' + YMDH + '.log'

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s %(funcName)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=filename,
                    filemode='w')