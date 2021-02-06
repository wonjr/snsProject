from django.conf.urls import url
from django.urls import path

from account import views
from account.views import index


urlpatterns = [
    path('', index, name='index'),
    url('', views.show, name='show'), #보여줄 때는 url?
    #url('', views.index, name='index'),
]
