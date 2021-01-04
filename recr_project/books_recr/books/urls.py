from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-home'),
    path('authors/', views.authors, name='books-authors'),
    path('publishers/', views.publishers, name='books-publishers'),
    path('about/', views.about, name='books-about')
]
