"""bks URL Configuration

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
# from bks.views import hello, goodbye, current_datetime, hours_ahead, request_meta, search_form, search
from bks.views import hello, goodbye, current_datetime, hours_ahead, request_meta, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('goodbye/', goodbye),
    path('time/', current_datetime),
    path('time/<int:h_ahead>/', hours_ahead),
    path('request-meta/', request_meta),
    # path('search_form/', search_form),
    path('search/', search),
]
