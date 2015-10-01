"""work URL Configuration

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

urlpatterns = [
    url(r'^$', 'web.views.index'),
    url(r'^edit_task/', 'web.views.edit_task', name='edit_task'),
    url(r'^show_tasks/', 'web.views.show_tasks', name='show_tasks'),
    url(r'^add_new_task/', 'web.views.add_new_task', name='show_tasks'),
    url(r'^save_task/', 'web.views.save_task', name='show_tasks'),
]
