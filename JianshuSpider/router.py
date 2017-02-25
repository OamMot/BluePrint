# -*- coding: utf-8 -*-
from flask import render_template, request, Flask
from JianshuSpider import jianshu
from JianshuSpider.service.getSpiderData import *
import json

@jianshu.route('/hello', methods=['GET'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def index():
    pn = int(request.args.get('pn', 1))
    rn = int(request.args.get('rn', 10))
    arrOutput = getSpiderData(pn, rn)
    return json.dumps(arrOutput, ensure_ascii=False)