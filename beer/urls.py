from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^write/$', views.list, name='write'),
    url(r'^login/$', views.list, name='login'),
]