"""prexp_priendship URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
	url(r"^$", "wjapp.views.analyze"),
	url(r"^reg/network/([\w \[\]\.]+)/", "wjapp.views.reg_network"),
	url(r"^reg/db/([\w \[\]\.]+)/", "wjapp.views.reg_db"),
	url(r"^export/([\w \[\]\.]+)/", "wjapp.views.export_all_db"),
	url(r"lwj/vis/", "wjapp.views.lwj_visualize"),
	url(r"vote/vis/", "wjapp.views.vote_visualize"),
]
