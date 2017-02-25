# -*- coding: utf-8 -*-
from flask import render_template
from ZhihuSpider import zhihu

@zhihu.route('/hello')  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def index():
    return 'zhihuget'