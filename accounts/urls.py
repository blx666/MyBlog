from django.conf.urls import url, include
from accounts.view import *

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#
# dajaxice_autodiscover()

urlpatterns = [
    url(r'^register/$', RegisterHandlerView.as_view(), name='register-handler'),
    url(r'^api/user/register/$', register, name='register'),
    url(r'^login/$', LoginHandlerView.as_view(), name='login-handler'),
    url(r'^api/user/login/$', login2, name='login2'),

    url(r'^api/user/loginout/$', loginout, name='loginout'),

    url(r'^loadfile/$', loadfileHander, name='loadfile-handler'),
    url(r'^api/loadfile/$', loadfile, name='load-file'),
    url(r'^api/filter/$', filter_category, name='filter-category'),
    url(r'^eamil/$', sender_user_mail, name='email'),

    url(r'^articles/$', viewArticles, name='articles'),
    url(r'^test-ajax/$', test_django_ajax, name='test_ajax'),




    url(r'^temp/$', LoadTemp.as_view(), name='temp'),

    # url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),


]

# urlpatterns += staticfiles_urlpatterns()

