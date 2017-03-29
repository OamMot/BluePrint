# -*- coding: utf-8 -*-
from flask import Flask
from ZhihuSpider import zhihu
from JianshuSpider import jianshu
from User import user
from LogModule.log import *
import time

application = Flask(__name__)

# blueprint router register
application.register_blueprint(zhihu, url_prefix='/zhihu')  # 注册asset蓝图，并指定前缀。
application.register_blueprint(jianshu, url_prefix='/jianshu')  # 注册asset蓝图，并指定前缀。
application.register_blueprint(user, url_prefix='/user')  # 注册asset蓝图，并指定前缀。

# init_log('./log/app')
YMDH = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
init_log('./logs/' + YMDH + '.log', application.logger)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)  # 运行flask http程序，host指定监听IP，port指定监听端口，调试时需要开启debug模式。