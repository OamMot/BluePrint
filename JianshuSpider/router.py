# -*- coding: utf-8 -*-
from flask import render_template, request, Flask
from JianshuSpider import jianshu
from JianshuSpider.service.getSpiderData import *
import json

@jianshu.route('/hello', methods=['GET'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def index():
    pn = int(request.args.get('pn', 1))
    rn = int(request.args.get('rn', 10))
    arrResponse = getSpiderData(pn, rn)
    arrOutput = {}
    arrOutput['errno'] = 0
    arrOutput['errmsg'] = 'success'
    arrOutput['data'] = arrResponse
    return json.dumps(arrOutput, ensure_ascii=False)

@jianshu.route('/followJianshuUser', methods=['GET'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def followJianshuTopic():
    user_id = int(request.args.get('user_identify', 0))
    user_identify = str(request.args.get('user_identify', ''))
    topic_identify = str(request.args.get('topic_identify', ''))
    spider_type = int(request.args.get('spider_type', 0))

    #用户信息入库，记录他关注了哪个话题

    #新的链接插入到库里

    #
