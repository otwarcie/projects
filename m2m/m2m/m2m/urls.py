"""m2m URL Configuration

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
from m2m_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.courses_list, name='courses_list'),
    path('students/', views.students_list, name='students_list'),
    path('students/<int:student_pk>', views.student_detail, name='student_detail'),
    path('students/add', views.student_add, name='student_add'),
    path('students/<int:student_pk>/enroll', views.course_enroll, name='course_enroll'),
    path('courses/<int:course_pk>', views.course_detail, name='course_detail'),
    path('courses/add', views.course_add, name='course_add'),
    path('courses/<int:course_pk>/enroll', views.student_enroll, name='student_enroll'),
]
