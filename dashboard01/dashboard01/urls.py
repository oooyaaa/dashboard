"""dashboard01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from board import views

urlpatterns = [
    
    path('',views.main),
    path('admin/', admin.site.urls), #admin 하면 들어가는게 이거때문임
        #장고는 기본적으로 만들어져있음
    
    path('list/',views.list),
    # path('cctv_map/',views.cctv_map),
    path('map/',views.map),
    path('result/',views.result),
    
]
