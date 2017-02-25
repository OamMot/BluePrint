# -*- coding: utf-8 -*-
import urllib2
import urllib
import requests
import json
import re
from bs4 import BeautifulSoup

def outputData(data_score, answer_link, title, user_name, user_link, summary):
    answer_link = answer_link.split('/')
    question_id = answer_link[2]
    answer_id = answer_link[4]
    user_id = ''
    if user_link != '':
        user_link = user_link.split('/')
        user_id = user_link[2]

    title = title.strip()
    print '------------------------------'
    print 'timestamp : ', data_score
    print 'answer_id : ', answer_id
    print 'question_id : ', question_id
    print 'user_id : ', user_id
    print 'user_name : ', user_name
    print 'title : ', title
    print 'summary : ', summary
    print '------------------------------'

def getAllInfoFromHtml(html) :
    line = html

    soup = BeautifulSoup(line)
    # print soup
    # print soup.prettify()
    data_score = soup.div['data-score']
    data_score = float(data_score)

    answer = soup.link['href']
    answer1 = answer
    str1 = answer1.split('/')

    # title = soup.link.div.div.h2.a.string
    findTitle = soup.link.div.div
    title = ''
    if findTitle is None:
        # print soup.prettify()
        return
    else:
        title = findTitle.h2.a.string

    user_first_step = soup.link.div.div.div
    # print user_first_step

    user_name_str = str(user_first_step)
    user_first_soup = BeautifulSoup(user_name_str)
    # print user_first_soup.prettify()

    user_second_step = user_first_soup.link.div.next_sibling.next_sibling.next_sibling.next_sibling
    user_name_str = str(user_second_step)
    user_second_soup = BeautifulSoup(user_name_str)
    # print user_second_soup.prettify()

    user_name = user_second_step.span.span
    user_link = ''
    if user_name is None:    #匿名用户
        user_name = user_second_step.span.string
    else:
        user_name = user_name.a.string
        user_link = user_second_step.span.a['href']
    answerLink = soup.link['href']

    # title_step = user_second_step.next_sibling.next_sibling.next_sibling
    summary_tag = soup.find('textarea')
    summary = summary_tag.string

    outputData(data_score,answerLink,title,user_name,user_link,summary)

def spider():
    header = {
        'Origin': 'https://www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'X-DevTools-Emulate-Network-Conditions-Client-Id': 'c7c0fc2d-c15c-48b8-a395-c9b4d08bb75d',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrftoken': '5b94aef64d1b05f50345b10e29b685b2',
        'Referer': 'https://www.zhihu.com/topic',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'd_c0="ADBAdo8iJwqPTjaoLRp2Cch6GEYEMxCQ41I=|1467204997"; _za=d3c44816-c586-45ed-baca-696258c4fa80; _zap=9c073a78-af58-42d7-950c-1aa0aadc630a; _ga=GA1.2.1649591047.1482679813; aliyungf_tc=AQAAAPs8jSBUrwAAUqmHPXa367fXAUAA; _xsrf=5b94aef64d1b05f50345b10e29b685b2; l_cap_id="ZjFiNDdjYzI5ODRiNDliODgyMjRjYmQxNDI0ZTk3MmU=|1484619491|1a5f4bb8e77d9c9ea6fb570dd2b60b82d848df2d"; cap_id="YWNlMGM2ZjA4ODEyNDcxNWI3OTgxZmQ3YjQ1YjY0Yzg=|1484619491|ea15e0faf9d7078660a2c1d2c5d9f83417e99f13"; r_cap_id="MDcyODU3NTlkNGVkNGJkN2E2YTNkOTIyMjJiN2I1OGI=|1484619492|ee8c5bdfdb6336698a59502c57965421a04f3f4e"; login="MTk4NzVmNWMyYTg2NGUxODhmZmQ2OGE5ZWU5YzAxMWM=|1484619497|8d85a080457cf34efd6bbb848573a11f4107490d"; n_c=1; s-q=%E9%99%86%E5%A5%87; s-i=1; sid=3h08lp9g; s-t=autocomplete; q_c1=89468bc122f2484fafc5845c8b8e379b|1485999373000|1482915417000; __utma=51854390.1649591047.1482679813.1485999378.1486003119.4; __utmb=51854390.0.10.1486003119; __utmc=51854390; __utmz=51854390.1485999378.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20140706=1^3=entry_date=20140706=1; z_c0=Mi4wQUFEQWJtZ3lBQUFBTUVCMmp5SW5DaGNBQUFCaEFsVk42Z3VsV0FBTllQcHVtVDdBMWNlX3VyX3FydnJzMS16cFNR|1486003118|51c02f5fb7aa065e908f1c8cafe6b47ce4bc34c1',
    }
    post = {
        'method': 'next',
        'params': '{"offset":0,"topic_id":46,"feed_type":"timeline_feed"}'
        # 'params': '{"offset":0,"topic_id":46,"feed_type":"smart_feed"}'
    }

    host = 'https://www.zhihu.com/node/TopicFeedList'
    req = requests.post(host, headers=header, data=post)
    json_str = req.json()

    html = json_str['msg']
    sum = 0

    for key in html:
        sum = sum + 1
        getAllInfoFromHtml(key)


def main():
    spider()

if __name__ == "__main__":
    main()