from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books-books'),
    path('authors/', views.authors, name='books-authors'),
    path('publishers/', views.publishers, name='books-publishers'),
#    path('book-detail/', views.book_detail, name='book-detail')
	path('<int:book_id>/', views.book_detail, name='book-detail')
]
