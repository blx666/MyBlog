#coding:utf-8
from django.conf.urls import url

from . import view

urlpatterns = [

    url(r'^file/$', view.UploadFile,name='UploadFile'),
    # url(r'^(?P<slug>[-\w]+)/$', view.userinfoDetailView.as_view(), name='article-detail'),   ?P<po_id>\d+
    url(r'^(?P<slug>\d+)/$', view.userinfoDetailView.as_view(), name='userinfo-detail'),
    url(r'^temp/$', view.TempView.as_view(), name='temp-detail'),
    url(r'^serializer/$', view.serializerStudents, name='serializer-score'),

]