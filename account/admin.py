from django.contrib import admin

# Register your models here.
from account.models import Data


class auth(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']
admin.site.register(Data, auth)