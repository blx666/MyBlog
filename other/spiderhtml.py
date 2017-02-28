# coding:utf-8
# url http://www.usd-cny.com/
from pyquery import PyQuery as pq


# from lxml import etree
# import lxml
# '''
#     name code symbol display
#     英镑　GDP   G      09
# '''

# first
# v_source = pq(url='http://www.usd-cny.com/')
# v_source('tr')
# for data in v_source('table')[4]:
    # print pq(data).text()
    # for data_child in data:
    #     print pq(data_child).text()

    # for data2 in pq(data).text():
    #     print pq(data2).text()
    # print pq(data).text()
    # for i in range(len(data)):
    #     if i == 0:
    #         continue
    #     tr = pq(data).find('tr').eq(i).text()
    #     for j in range(len(tr)):
    #         print tr[j]
# first

# second
# v_source = pq(url='http://www.usd-cny.com/')
# v_source('tr')
# length = len(v_source('table')[4])
# for data in v_source('table')[4]:
#     # for i in
#     print pq(data).text()

# for i in range(length):
#     if i == 0:
#         continue
#     else:
#         for data in v_source('table')[4][i]:
#             print pq(data).text()
        # print pq(v_source('table')[4][i][0]).text()
        #
        # print pq(v_source('table')[4][i][1]).text()

# second

# worong 由于pq抓取的数据和网页原版的数据不一致！！！　换一种方法

# beautiful soup4 spider

from bs4 import BeautifulSoup
import urllib2
response = urllib2.urlopen('http://www.usd-cny.com/')
html_page = response.read().decode('gbk')
# print html_page
soup = BeautifulSoup(html_page, 'html.parser')
# print (soup.prettify())  # 获取的网页格式化　排版整齐和直接获取的不一样
print soup.title.name
# find_all('tag')
# print soup.find(height="113", width='777')
table = soup.find_all('table')

# print table[4]  # 当前的table 包含所有的兑换规则
# soup_table = BeautifulSoup(table[4], 'html.parser')
# print (soup_table.prettify())

# print table[4].table


# tag = soup.table
# print tag
# print type(tag)
# second


# third
import urllib.request
import json
response = urllib.request.urlopen('http://api.fixer.io/latest?base=USD')
html = json.loads(response.read())
print html
print html['rates']















