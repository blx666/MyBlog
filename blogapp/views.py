#-*-coding:utf-8-*-
import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import loader

from blogapp.models import UserBlog, Blog, Comment
from blogapp.forms import userForm
from django.shortcuts import render, get_object_or_404   ##提供网页  ！！

from rest_framework.parsers import JSONParser
from django.template import Template, Context
from django.core.cache import cache
from blogapp.forms import CalendarWiget, LoinForm

from blogapp import Serializer
from utils.tools import *
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def register(request):
    template = loader.get_template('blogapp/register.html')
    contents = {}
    # return HttpResponse(templateRegister.render(contents,request))
    return HttpResponse(template.render(contents,request))

    #  return HttpResponse('zhuce页面')
    # pass


# 主要联系include函数　　个人理解是include 应用其他模板的时候，同时发送了引用这个模板的请求
def includeTemplate(request):
    dict1 = {'name': 'blx', 'age': 23}
    t = loader.get_template('blogapp/include.html')

    c = Context({'respose': dict1})
    html = t.render(c)
    return HttpResponse(html)
    # return
    # pass


def registerHandler(request):
    name = request.POST['name']
    pwd = request.POST['pwd']
    phoneNumber = request.POST['phoneNumber']
    # userModel =UserBlog(name=name, pwd =pwd, phone=phoneNumber)
    # userModel.save()
    User.objects.create_user(name, pwd)

    # return
    return  HttpResponseRedirect(reverse('login' ))
    # pass


def login(request):
    template = loader.get_template('blogapp/login.html')
    today_time = datetime.datetime.now()
    contents = {'today_time':  today_time, 'default': "123", 'login_form': LoinForm()}

    return HttpResponse(template.render(contents, request), contents)
    # return HttpResponse('登陆页面')
    # pass


def loginHandler(request, page):
    page = page
    if page:
        blogs = UserBlog.objects.all()  # Get released blogs
        paginator = Paginator(blogs, 2)  ##,每行都显示的数据
        try:
            blogs = paginator.page(page)  ## 当前的页码
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        return render(request, 'blogapp/publishblog.html', {'blogs': blogs})



def publishblog(request):

    ##分页

    blogModelList = Blog.objects.all()
    # blog_list = Paginator(blogModelList,1,1)

    template = loader.get_template('blogapp/publishblog.html')

    # for blogModel in blogModelList:

    contents = {'blogModelList': blogModelList}
    return HttpResponse(template.render(contents, request))

    # return HttpResponse('发布博客')
    # pass

def publishblogHandler(request):
    content = request.GET['blogcomment']
    userid = request.GET['userid']
    if userid == '':
        return render(request,'blogapp/login.html')

    blogModel = Blog()
    blogModel.userid_id = userid
    blogModel.content = content
    blogModel.save()
    blogModelList = Blog.objects.all()
    return render(request, 'blogapp/publishblog.html',{'userid':userid, 'blogModelList':blogModelList})
    # return HttpResponse('1232')


def publishcomment(request):
    ##使用一个form类
    content = request.POST['comment']
    blogid=request.POST['blogid']
    commentModel = Comment()
    commentModel.content = content
    commentModel.blogid_id = blogid
    commentModel.save()
    blogModelList = Blog.objects.all()
    return render(request, 'blogapp/publishblog.html',{'blogModelList':blogModelList})

def error(request):
    return render(request, 'blogapp/error.html')

def returncookie(request):
    return HttpResponseRedirect(reverse('returncookie'))
    # tremplate = loader.get_template('blogapp/register.html')
    # context  = {"name":"blx"}
    # html = tremplate.render(context,request)
    # return HttpResponse(html)


def update_user(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        instance = UserBlog.objects.get(id=2)
        if form.is_valid():
            data = {}
            for field in form.changed_data:
                data[field] = form.cleaned_data[field]
            for key ,value in data.items():
                setattr(instance, key, value)
            instance.save()
            HttpResponse('OK!')
        else:
            HttpResponse(form.errors)


def serializers(request):
    if request.method == 'GET':
        snippets = Serializer.Snippet.objects.all()
        serializer = Serializer.SnippetSerializer(snippets, many=True)
        return HttpResponse(serializer.data)
    # serializer = Serializer.SnippetSerializer(data=request.data)
    # serializer.save()
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer.SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        return HttpResponse(serializer.errors, status=400)
    # pass












