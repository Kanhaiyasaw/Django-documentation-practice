from django.contrib import admin
from polls.models import *

@admin.register(Question)
class som_fun(admin.ModelAdmin):
    pass

@admin.register(Choice)
class reg_fun(admin.ModelAdmin):
    pass
