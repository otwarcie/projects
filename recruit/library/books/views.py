from django.shortcuts import render
from .models import Book, Author, Publisher, WrittenBy
from django.http import HttpResponse

'''
def home(request):
	return HttpResponse('<h1>List of books, I hope</h1>')
'''

def books(request):
	context = {
		'books': Book.objects.all()
	}
	return render(request, 'books/books.html', context)

def book_detail(request, book_id):
	return HttpResponse('You are trying to look at book ' % book_id)
#	return render(request, 'books/books.html', book_id)

def authors(request):
	context = {
		'authors': Author.objects.all()
	}
	return render(request, 'books/authors.html', context)

def publishers(request):
	context = {
		'publishers': Publisher.objects.all()
	}
	return render(request, 'books/publishers.html', context)

