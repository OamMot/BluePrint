# -*- coding: utf-8 -*-
from flask import Flask
from ZhihuSpider import zhihu
from JianshuSpider import jianshu
apple = Flask(__name__)

# blueprint router register
apple.register_blueprint(zhihu, url_prefix='/zhihu')  # 注册asset蓝图，并指定前缀。
apple.register_blueprint(jianshu, url_prefix='/jianshu')  # 注册asset蓝图，并指定前缀。

if __name__ == '__main__':
    apple.run(host='0.0.0.0', port=5000, debug=True)  # 运行flask http程序，host指定监听IP，port指定监听端口，调试时需要开启debug模式。