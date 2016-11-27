"""mysite0910 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#import sys
#sys.path.append('C:\Users\luck\Desktop\django_practice\mysite0910')
#for s in sys.path:
    #print s
    #print sys.path.index(s)

#print sys.path[0]
#from restaurants import views



#from mysite import views

from restaurants.views import menu,list_restaurants,meta,welcome,comment,set_c,get_c,use_session,index,login,logout
#import os

#print os.environ['DJANGO_SETTINGS_MODULE']
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


from django.conf.urls import include, url
from django.contrib import admin
from  views import test
#from views import menu
from restaurants.views import menu,list_restaurants,meta,welcome,comment,set_c,get_c,use_session,index,login,logout
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/(\d{1,5})/$',menu),
    #url('r^welcome/$',welcome),
    url(r'^restaurants_list/$',list_restaurants),
    url(r'^test/$',test),
    url(r'^meta/$',meta),
    url(r'^welcome/',welcome),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^test_session/$',use_session ),
    url(r'^index/$', index),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout)
]
