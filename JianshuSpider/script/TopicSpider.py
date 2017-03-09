# -*- coding: utf-8 -*-
from urllib import urlencode
import requests
import time
import logging
from bs4 import BeautifulSoup

import sys
sys.path.append("../../../BluePrint/")

from JianshuSpider.service.insertSpiderData import *
from JianshuSpider.service.getSpiderData import *

def outAllData(allJianshuInfo):
    print '--------------------------------------------------------'
    for all in allJianshuInfo:
        print 'title : ' + all['title']
        print 'summary : ' + all['summary']
        print 'topic_identify : ' + all['topic_identify']
        print 'user_name : ' + all['user_name']
        print 'user_identify : ' + all['user_identify']
    print '--------------------------------------------------------'


def getAllInfoFromHtml(html = '', pool_id = 0) :

    soup = BeautifulSoup(html)
    data_score = soup.ul
    li = data_score.findAll('li')

    sum = 0
    allJianshuInfo = []
    for small_li in li:
        user_info = small_li.find('a', {"class" : "blue-link"})
        #获取用户名
        user_name = user_info.text
        #获取用户链接
        user_identify = user_info['href']
        #获取发布时间
        now_time = small_li.find('span', {"class" : "time"})
        published_at = now_time['data-shared-at']
        published_at = published_at[0:10] + " " + published_at[11:19]
        time.strptime(published_at, '%Y-%m-%d %H:%M:%S')
        #发布时间戳
        published_at = int(time.mktime(time.strptime(published_at, '%Y-%m-%d %H:%M:%S')))
        #入库时间戳
        inserted_at = time.time()

        topic_info = small_li.find('a', {"class" : "title"})
        #文章标题
        title = topic_info.text
        #文章标识（链接）
        topic_identify = topic_info['href']
        #文章摘要
        topic_abstract = small_li.find('p', {"class" : "abstract"})
        summary = topic_abstract.text
        sum = sum + 1 #维护个数

        allJianshuInfo.append({'user_name' : user_name,
                               'user_identify' : user_identify,
                               'published_at' : published_at,
                               'inserted_at' : inserted_at,
                               'title' : title,
                               'topic_identify' : topic_identify,
                               'summary' : summary,
                               'pool_id' : pool_id
                               })
    return allJianshuInfo

def spider_first(topic_identify = ''):
    referer = 'http://www.jianshu.com/c/' + topic_identify
    header = {
        'Accept': 'text/html, */*; q=0.01',
        'X-DevTools-Emulate-Network-Conditions-Client-Id': '517e2929-c72f-44a8-b9cb-ef4e664b6c2f',
        'X-CSRF-Token': '1bwqUMxKP5xqu7HQZnT8i5Vp+2COCQugNRlyquf2RJ/VXMHbgm/CYJmAsHEPPeJcqNv/D2FQ8Wco5/HphYO6mA==',
        'X-Requested-With': 'XMLHttpRequest',
        'X-PJAX': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Referer': referer,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1467353185,1468731500,1469142570,1469410134; __utma=194070582.1875603163.1467337403.1474610433.1474973865.12; __utmz=194070582.1474973865.12.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=194070582.|2=User%20Type=Visitor=1; signin_redirect=http%3A%2F%2Fwww.jianshu.com%2Fc%2Fa40d54e10b51; CNZZDATA1258679142=25146178-1474969231-https%253A%252F%252Fwww.baidu.com%252F%7C1487658049; _ga=GA1.2.1875603163.1467337403; _session_id=S09wam1yRDV5OUVKOWpSVlZzc1pWOFdFUUkvZUlhb2wrN0FKVCtLRmR4Y1RpTnhqcGx5UFVTcWFKUW1JR2NlNUFWVkV3OHZ0dDVScVFlTlFxTVVCV3Q4WUtWN2tZOEYyOXZNWkdQWFBnWUJha1g0MGs2WFMxZjViQ1Q0ZThiaElDeFdhWXRsSEFZdGZHR2R0VTlUZzY1c2ptNWhTUEN6aUVGLzR6blZLMi9UR1gveXo1dmp1NVJ3VUZ5MnlOYjFGeTBrcGNIeEEzc2hBUlE4ZUJodGo3UFdTbzJhZkh4a05ZWjh3SWJJOHZ5aXd3UmlWV3ZucVpDZlJ1R0I0R2tybldIT1hONDVrczErbmcvRkN5bGEvV0Vkb1d0WmdGclZPTlM3UXVTR0tBVC9UdmNxY1ZPTEJpYnBWS1BYTHV2WUFuYUMvVER4VVMvcnVDd3EwbXRNRGFnPT0tLXJ2N2dtUFVwZEZvWDNSNUdycUlnc2c9PQ%3D%3D--6f17df101719aec488e029d05f0273281026bc21'
    }
    post = {
        'params': '{"order_by":"added_at","_pjax":"#list-container"}'
        # 'params': '{"offset":0,"topic_id":46,"feed_type":"smart_feed"}'
    }

    host = 'https://www.jianshu.com/c/' + topic_identify +'?order_by=added_at&_pjax=%23list-container'
    req = requests.post(host, headers=header, data=post)
    json_str = req.text
    allJianshuInfo = getAllInfoFromHtml(json_str)
    haveRepeat = insertData(allJianshuInfo)
    return haveRepeat
    # 1: 有重复
    # 0: 无重复

def spider_remain(topic_identify = '', pool_id = 0):
    referer = 'http://www.jianshu.com/c/' + topic_identify
    header = {
        'Accept': 'text/html, */*; q=0.01',
        'X-DevTools-Emulate-Network-Conditions-Client-Id': '517e2929-c72f-44a8-b9cb-ef4e664b6c2f',
        'X-CSRF-Token': '1bwqUMxKP5xqu7HQZnT8i5Vp+2COCQugNRlyquf2RJ/VXMHbgm/CYJmAsHEPPeJcqNv/D2FQ8Wco5/HphYO6mA==',
        'X-Requested-With': 'XMLHttpRequest',
        'X-PJAX': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Referer': referer,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1467353185,1468731500,1469142570,1469410134; __utma=194070582.1875603163.1467337403.1474610433.1474973865.12; __utmz=194070582.1474973865.12.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=194070582.|2=User%20Type=Visitor=1; signin_redirect=http%3A%2F%2Fwww.jianshu.com%2Fc%2Fa40d54e10b51; CNZZDATA1258679142=25146178-1474969231-https%253A%252F%252Fwww.baidu.com%252F%7C1487658049; _ga=GA1.2.1875603163.1467337403; _session_id=S09wam1yRDV5OUVKOWpSVlZzc1pWOFdFUUkvZUlhb2wrN0FKVCtLRmR4Y1RpTnhqcGx5UFVTcWFKUW1JR2NlNUFWVkV3OHZ0dDVScVFlTlFxTVVCV3Q4WUtWN2tZOEYyOXZNWkdQWFBnWUJha1g0MGs2WFMxZjViQ1Q0ZThiaElDeFdhWXRsSEFZdGZHR2R0VTlUZzY1c2ptNWhTUEN6aUVGLzR6blZLMi9UR1gveXo1dmp1NVJ3VUZ5MnlOYjFGeTBrcGNIeEEzc2hBUlE4ZUJodGo3UFdTbzJhZkh4a05ZWjh3SWJJOHZ5aXd3UmlWV3ZucVpDZlJ1R0I0R2tybldIT1hONDVrczErbmcvRkN5bGEvV0Vkb1d0WmdGclZPTlM3UXVTR0tBVC9UdmNxY1ZPTEJpYnBWS1BYTHV2WUFuYUMvVER4VVMvcnVDd3EwbXRNRGFnPT0tLXJ2N2dtUFVwZEZvWDNSNUdycUlnc2c9PQ%3D%3D--6f17df101719aec488e029d05f0273281026bc21'
    }
    post = {
        'params': '{"order_by":"added_at","page":"#list-container"}'
    }

    for i in range(1, 10):
        time.sleep(3)
        host = 'https://www.jianshu.com/c/' + topic_identify +'?order_by=added_at&page=' + str(i)
        #verify=False 去掉会导致认证证书失败？
        try:
            req = requests.post(host, headers=header, data=post, verify=False, timeout=1)
        except requests.exceptions.RequestException:
            logging.warning('connect timeout', host)
            return 0
        json_str = req.text
        allJianshuInfo = getAllInfoFromHtml(json_str, pool_id)
        haveRepeat = insertData(allJianshuInfo)
        if (haveRepeat == 1) :
            return 1;
    return 0

def main():
    # topic_identify = '20f7f4031550'
    while (1) :
        topic_identifys = []
        for i in range(1, 1000000) :
            topic_identifys = getSpiderPool(i, 100) # 可优化
            print topic_identifys
            logging.warning('topic_identifys', topic_identifys)
            for ob_topic_identify in topic_identifys:
                topic_identify = ob_topic_identify['identify']
                pool_id = ob_topic_identify['pool_id']
                spider_remain(topic_identify, pool_id)
            if (len(topic_identifys) < 100):
                break;


if __name__ == "__main__":
    main()