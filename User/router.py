# -*- coding: utf-8 -*-
from flask import render_template, request, Flask
from User import user
from service.login import *
from service.followSomething import *
import json

@user.route('/login', methods=['GET'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def index():
    nickname = str(request.args.get('nickname', ''))
    description = str(request.args.get('description', ''))
    avatar = str(request.args.get('avatar', ''))
    arrOutput = []
    return json.dumps(arrOutput, ensure_ascii=False)

@user.route('/followSomething', methods=['GET'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def followJianshuTopic():
    user_id = int(request.args.get('user_id', 0))
    type = int(request.args.get('type', 0))
    identify = str(request.args.get('identify', ''))
    followTopic(user_id, type, identify)

    return 'success'
    #用户信息入库，记录他关注了哪个话题

    #新的链接插入到库里

    #
