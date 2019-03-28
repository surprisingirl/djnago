"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from store import views
from django.conf.urls import url



urlpatterns = [
    url(r'^$', views.home, name='home'),
   
    url(r'^category/(?P<pk>\d+)/', views.category, name='category'),
    url(r'category/new', views.new_category, name='new_category'),
    url(r'recipe/(?P<pk>\d+)/', views.recipe, name='recipe'),
    url(r'recipe/new', views.new_recipe, name='new_recipe'),
    
    
   
]
   


    
