
from django.contrib import admin

from blogapp.models import *



admin.site.register(UserBlog)
admin.site.register(Blog)
admin.site.register(Comment)

