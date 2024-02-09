"""ExampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from VVITApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('g/',views.demo),
    path('k/<str:n>/',views.greet),
    path('gh/<str:m>/<int:a>/',views.stdnt),
    path("eh/",views.ky),
    path("ab/",views.inline),
    path("bc/<str:x>/<int:y>/",views.internal),
    path("hi/<str:a>/",views.jsalert),
    path("hello/<str:n>/<str:b>/<int:r>/<int:y>/",views.info),
    path("cd/",views.np),
    path("de/<str:n>/<str:s>/<str:r>/",views.pp),
    path("ef/",views.dr),
    path('',include('BSApp.urls')),
]
