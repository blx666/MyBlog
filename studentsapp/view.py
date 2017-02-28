#coding:utf-8
from studentsapp.models import UserGroup,UserInfo,UserProfile,Host

from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.template import Template , Context

from studentsapp.form import FileForm
import logging

logger = logging.getLogger(__name__)


from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.utils import timezone

from studentsapp.models import UserInfo




def profileHanlerd(request):
    pass
def upload_file(request):
    if request.method == "POST":
        obj = request.FILES.get('fafafa')
        f = open(obj.name, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
    return render(request, 'studentsapp/../blogapp/templates/file.html')

log = logging.getLogger('test1')

def UploadFile(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'students/file.html', {})
    # return render(request, 'studentsapp/file.html')
    if request.method == 'POST':
        uf = FileForm(request.POST, request.FILES)

        if uf.is_valid():
            template = models.UploadFile()
            template.userid = 1
            template.file = uf.cleaned_data['ExcelFile']
            template.save()

            print (template.file)
    else:
        fileform  = FileForm()
        try:
            user_group = UserGroup.objects.get(id=1)
        except Exception,e:
            logger.error(e)

        ##给usergroup　帮顶user信息
        userinfo = {}
        for userid in user_group.user_info.values_list('id', flat=True):
            if userid not in userinfo:
                userinfo[userid] = UserInfo.objects.get(id=userid)

        user_group.users = userinfo.values()

        from django.core.mail import send_mail
        subject = 'test email'
        message ='This is my first email'

        send_mail(subject, message, '139@qq.com', [user_group], connection=None, html_message=None)
        log.info('message')

        return render(request, 'students/file.html', {'fileform': fileform, 'usergroup': user_group})


class userinfoDetailView(DetailView):
    model = UserInfo
    def get_context_data(self, **kwargs):
        context = super(userinfoDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TempView(TemplateView):
    template_name = "students/templateview.html"
    # model = UserInfo

    def get_context_data(self, **kwargs):
        context = super(TempView, self).get_context_data(**kwargs)
        context['latest_articles'] = UserInfo.objects.all()
        return context



    # context_object_name = 'dreamreals_objects'



from rest_framework.parsers import JSONParser
from django.template import Template,Context

from blogapp import Serializer

from utils.tools import *


def serializerStudents(request):
    data = JSONParser().parse(request)
    serializer = Serializer.StudentSerialiter(data=data)
    if serializer.is_valid():
        print ('123')

from django.core.cache import cache







