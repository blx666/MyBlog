#coding:utf-8
from django.db import models


class UserProfile(models.Model):
    user_info = models.OneToOneField('UserInfo')
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


    def __unicode__(self):
        return self.username


class UserInfo(models.Model):
    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户'),
    )
    user_type = models.IntegerField(choices=user_type_choice, )
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=128)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'User_Info'
        verbose_name_plural = 'User_Info'


class UserGroup(models.Model):

    caption = models.CharField(max_length=64)

    user_info = models.ManyToManyField('UserInfo')

    def __unicode__(self):
        return self.caption

    def get_UserInfo_display(self):
        return ','.join(self.user_info.values_list('name'))


class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    user_group = models.ForeignKey('UserGroup')

    def __unicode__(self):
        return self.hostname


class UploadFile(models.Model):
    userid = models.CharField(max_length=30)
    file = models.FileField(upload_to='./template/')
    date = models.DateTimeField(auto_now_add=True)





