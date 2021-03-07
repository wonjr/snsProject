from django.conf.urls import url
from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:form_id>/', views.show, name='show'),
]
