# -*- coding: utf-8 -*-
from flask import Flask
from ZhihuSpider import zhihu
from JianshuSpider import jianshu
from User import user
from LogModule.log import *
import time

apple = Flask(__name__)

# blueprint router register
apple.register_blueprint(zhihu, url_prefix='/zhihu')  # 注册asset蓝图，并指定前缀。
apple.register_blueprint(jianshu, url_prefix='/jianshu')  # 注册asset蓝图，并指定前缀。
apple.register_blueprint(user, url_prefix='/user')  # 注册asset蓝图，并指定前缀。

# init_log('./log/app')
YMDH = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
init_log('./logs/' + YMDH + '.log', apple.logger)

if __name__ == '__main__':
    apple.run(host='0.0.0.0', port=5000)  # 运行flask http程序，host指定监听IP，port指定监听端口，调试时需要开启debug模式。