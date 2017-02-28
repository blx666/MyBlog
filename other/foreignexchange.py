#!/usr/bin/env python
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from auth import Session
from bearth.apps.main.models import Currency   # bearth isfile
from bearth.utils.public.str_utils import str2float  # bearth isfile
from connection import Connection
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.core.management import call_command
from oscar.core.loading import get_model
import logging
import os
import re

Product = get_model('catalogue', 'Product')

START_URL = 'https://www.wellsfargo.com/foreignexchange/'
SEARCH_URL = 'https://www.foreignexchangeservices.com/index.html?partnerid=FES&serviceType=rate'
GOOGLE_URL = {'AUD': 'http://www.google.com/finance?q=USDAUD',
              'CAD': 'http://www.google.com/finance?q=USDCAD'} # 澳大利亚, 加拿大

class ForeignExchange(object):
    def __init__(self, session=None):
        self.conn = Connection()
        if session:
            self.conn.session = session
        else:
            self.conn.session = Session()

    def start_page(self, source='google', curr='CAD'):
        if source == 'google':
            import urllib
            response = urllib.urlopen(GOOGLE_URL[curr]).read()
            return response
        self.conn.do_get(START_URL)
        response = self.conn.do_get(SEARCH_URL)
        return response

    def getAllRates(self, source='google'):
        exchange_rates = {}
        if source == 'google':
            currs = ['CAD', 'AUD']
            for curr in currs:
                res = self.start_page(source, curr)
                bf = BeautifulSoup(res)
                cad_node = bf.find('span', {'class':'bld'})
                if cad_node:
                    cad_currency = re.findall(r'\d+.\d+', cad_node.string)
                    if cad_currency:
                        exchange_rates[curr] = cad_currency[0]
            return exchange_rates
        res = self.start_page(source)
        bf = BeautifulSoup(res)
        tb_div = bf.find('div', {'id':'subContentOne'})
        if tb_div:
            lines = tb_div.findAll('tr')
            for line in lines:
                tds = line.findAll('td')
                if len(tds) == 2:
                    currency = tds[0].string
                    if '(' in currency and ')' in currency:
                        currency = currency[currency.index('(')+1:currency.index(')')]
                        rate = str2float(tds[1].string.strip())
                        exchange_rates[currency] = round(1.0 / rate, 4) # since our system is using exchange rate like USDCAD, not CADUSD
        return exchange_rates

def email_admin(log):
    subject = 'Retrive Latest Currency'
    content = 'Exception occurred: %s' % log
    sender = settings.ADMINS[0][1]
    mail = EmailMessage(subject, content, sender, ['liuyan@aragoncs.com', 'liuyijun@aragoncs.com'])
    mail.content_subtype = 'html'
    mail.send()

if __name__ == '__main__':
    lock = 'get_currency.lock'
    if not os.path.isfile(lock):
        with open(lock, 'w'):
            pass
        try:
            exchange_site = ForeignExchange()
            all_rates = exchange_site.getAllRates('google')
            currency_data = Currency.objects.all()
            currency_updated = False
            for currency in currency_data:
                code, rate = currency.code, currency.currency
                rt_rate = all_rates.get(code)
                if rt_rate:
                    if str(rate) != str(rt_rate):
                        currency.currency = rt_rate
                        currency.save()
                        currency_updated = True
            if currency_updated:
                call_command('update_index', using=['product'])
        except Exception, e:
            email_admin(e)
            logging.exception('Got exception on main handler')
        finally:
            os.remove(lock)
    else:
        print "abnormal exit, if another thread is not running, please remove %s to continue" % lock

