#coding:utf-8
from django.contrib.auth.models import User
# from django.db import models
from django.contrib.gis.db import models
import hashlib

import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, )
    ##自定义方法和属性
    accepted_eula = models.NullBooleanField()
    favorite_animal = models.EmailField()
    habby = models.CharField(max_length=100, null=True)
    sex = models.NullBooleanField()
    avatar = models.FileField(upload_to='blogapp/static/img/', null=True)
    price = models.FloatField(help_text='there is a price', null=True, blank=True)

    # @property
    # def filename(self):
    #     return os.path.basename(self.attachment.name)
    #

class Category(models.Model):
    name = models.CharField('类别', max_length=128)

    class Meta:
        verbose_name_plural = '类别目录'
        verbose_name = '类别目录'


    def __unicode__(self):
        return self.name
    #
    # def __str__(self):
    #     return self.LocationName
    #

class Product(models.Model):
    name = models.CharField(max_length=128)
    category_id = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = '种类'
        verbose_name = '种类'

    # this method is relation about admin field show
    def __str__(self):
        return self.name

    @classmethod
    def create_token(cls, user):
        token = str(user.id) + str(user.email)
        md5token = hashlib.md5()
        md5token.update(token)
        token = md5token.hexdigest()
        return token

# class SouthTexasCity(models.Model):
#     name = models.CharField(max_length=30)
#     # A projected coordinate system (only valid for South Texas!)
#     # is used, units are in meters.
#     point = models.PointField(srid=32140)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=3)
    rate = models.FloatField(help_text='here is the rate base on dollar')
    display = models.CharField(max_length=3)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = "Currencies"







