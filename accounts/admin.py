from django.contrib import admin

from accounts.models import *

import sys
from imp import reload
reload(sys)

# sys.setdefaultencoding("utf8")
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(SouthTexasCity)

# class Articlaeadmin(admin.ModelAdmin):
#


