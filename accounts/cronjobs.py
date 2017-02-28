# coding:utf-8
# url http://www.usd-cny.com/
from pyquery import PyQuery as pq
from accounts.models import Currency


def add_category():
    # cate = Category()
    # cate.name = 'blx'
    # cate.save()
    cu = Currency()
    v_source = pq(url='http://www.usd-cny.com/')
    v_source('tr')
    length = len(v_source('table')[4])
    for i in range(length):
        if i != 0:
            money = pq(v_source('table')[4][i][0]).text().split()
            cu.name = money[0]
            cu.code = money[1]
            cu.symbol = list(money[1])[0]
            cu.rate = pq(v_source('table')[4][i][1]).text()
            cu.display = '1'
            cu.save()

            # print pq(v_source('table')[4][i][0]).text()  # code
            # print pq(v_source('table')[4][i][1]).text()  # 汇率
