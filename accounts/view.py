#coding:utf-8
from django.views.generic import TemplateView
from accounts.forms import RegistrationForm, UserProfileForm, UploadFileForm, CategoryForm
from accounts.models import UserProfile, Category, Product
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import send_mail
from django.conf import settings
import pytz
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.auth.models import User

class LoadTemp(TemplateView):
    template_name = 'accounts/abort.html'


class RegisterHandlerView(TemplateView):
    template_name = 'accounts/register.html'


class LoginHandlerView(TemplateView):
    template_name = 'accounts/login.html'
    print(pytz.all_timezones)


def loadfileHander(request):
    template = loader.get_template('accounts/file.html')
    content = {'form': UploadFileForm()}
    return HttpResponse(template.render(content, request))


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        accepted_eula = request.POST.get('accepted_eula', '')
        favorite_animal = request.POST.get('favorite_animal', '')

        is_exit_user = User.objects.filter(username=username).exists()
        if is_exit_user:
            return HttpResponse('user already exists!')
        ##用户自动登陆如果登陆成功说明已经注册，如果不能成功，在注册

        registerform = RegistrationForm({'username': username, 'password':  password})
        userProfileform = UserProfileForm({'accepted_eula': True, 'favorite_animal': favorite_animal}) ##'agency_email': agency_email, 'agency_address': agency_address
        if not registerform.is_valid():
            return HttpResponse(registerform.errors.values())
        if not userProfileform.is_valid():
            return HttpResponse(userProfileform.errors.values())
        user = User.objects.create_user(username=username, password=password)

        profile = UserProfile()
        profile.user = user
        profile.accepted_eula = accepted_eula
        profile.favorite_animal = favorite_animal
        profile.save()
        response = {
            'status': 0,
            'message': 'ok',
            'result': {'user_id': user.id}
        }
        return HttpResponse(response)


def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:

                login(request, user)
                # 重定向到一个登录成功页面。
                data = {'is_log': request.user.is_authenticated(), 'static': 'success'}
                return HttpResponse(data)
            else:
                return HttpResponse('user is die!')
        # 返回一个“帐户已禁用”错误信息。
        else:
            return HttpResponse('username or password is worng!')
        # 返回一个“非法用户名或密码”错误信息。
        pass


@login_required
def loginout(request):
    # return HttpResponse('hello world!')
    logout(request)
    data = {'is_log': request.user.is_authenticated(), 'static': 'fail'}
    return HttpResponse(data)
    # pass


def loadfile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            adminuser = User.objects.get(id=1)
            newuser = UserProfile()
            newuser.avatar = form.cleaned_data['userpic']
            newuser.user_id = adminuser.id
            newuser.accepted_eula = True
            newuser.favorite_animal = '166@qq.com'
            newuser.save()
            return HttpResponse('ok!')
        else:
            return HttpResponse('parameters is wronngs!')


def filter_category(request):
    nowtime = datetime.datetime.now()
    if request.method == 'POST':
        user = User.objects.get(id=5)
        token = Product.create_token(user)


        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            data = category_form.cleaned_data['name']
            result = Product.objects.filter(category_id__in=data)
        else:
            result = Product.objects.all()
        return render(request, 'accounts/filter.html', {'results': result, 'form': CategoryForm()})
    else:
        # cache.get('my_cache')
        return render(request, 'accounts/filter.html', {'form': CategoryForm(), 'nowtime': nowtime, 'my_cache': cache.get('my_cache')})


def sender_user_mail(request):
    # if request.method == 'POST':
    message = 'Upload invoice failed for CDP The error message is'
    send_mail('Portal Invoice error', message, '2332191547@qq.com', ['1392133729@qq.com'], fail_silently=True)


# @cache_page(1*60)
def viewArticles(request):
   up = UserProfile.objects.first()
   # text = "Displaying articles of 111222"
   cache.set('my_cache', 'my first cache app', 5*60)
   return HttpResponse(str(up.user)+'          '+str(up.favorite_animal))


# test django ajax
def test_django_ajax(request):
    return render(request, 'accounts/dreamreal.html')



def test_branch(request):

    pass