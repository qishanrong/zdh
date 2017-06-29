"""zdh URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app_zdh.views.login'),
    url(r'^login2/','app_zdh.views.login2'),
    url(r'^list/','app_zdh.views.servers_list'),
    url(r'^servers_fiter/','app_zdh.views.servers_fiter'),
    url(r'^add_server/','app_zdh.views.add_server'),
    url(r'^add/','app_zdh.views.add'),
    url(r'^grant_user/','app_zdh.views.grant_user'),
    url(r'^grant_add/','app_zdh.views.grant_user2'),
]
