#coding:utf-8
from django.conf.urls import url, include
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 主要联系include函数　　个人理解是include 应用其他模板的时候，同时发送了引用这个模板的请求
    url(r'^register/$', views.register, name='register'),

    url(r'^register/include', views.includeTemplate, name = 'includeTemplate'),

    url(r'^registerhandler/$', views.registerHandler, name='registerHandler'),
    url(r'^login/$', views.login, name='login'),


    url(r'^loginhandler(?P<page>\d+)/$',views.loginHandler, name='loginHandler'),
    # url(r'^record-(?P<record_id>\d+)/approve-cad-grow/$', 'approve_cad_grow', name='approve-cad-grow'),


    url(r'^publishblog/$',views.publishblog, name='publishblog'),
    url(r'^publishbloghandler/$',views.publishblogHandler, name='publishblogHandler'),

    url(r'^publishcomment/$', views.publishcomment, name='publishcomment'),
    url(r'^error/$', views.error, name='error'),

    url(r'^returncookie/$', views.returncookie, name='returncookie'),
    url(r'^ser/$', views.serializers, name='serializers'),


    url(r'^update-user/$', views.update_user, name='update-user'),

    # url(r'^next-page/', include('accounts.urls'))  主要使用include() 的用法　就是包含另外一个app的url


]