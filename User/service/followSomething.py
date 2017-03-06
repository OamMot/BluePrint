# -*- coding: utf-8 -*-
from User.dl.user_dl_solve import *

def followTopic(user_id = 0, type = 0, identify = ''):
    if (user_id <= 0) :
        return 0;
    #入库, 关注
    arrOutput = dlSelectSomething(user_id, type, identify)
    if (len(arrOutput) > 0):
        return 0
    dlFollowSomething(user_id, type, identify)
    arrOutput = dlSelectSomething(user_id, type, identify)
    pool_id = arrOutput[0]['pool_id']
    published_at = time.time()
    dlInsertUserSpiderPool(user_id, pool_id, published_at)
    #加入用户表

