from django.shortcuts import render
from .models import Book, Author, BookAuthor, Publisher
from django.http import HttpResponse

books = [
	{
		'title': 'Green Book Title',
		'publisher_id': 1,
		'pages_num': 100,
		'cover_image': 'Green Cover'
	},
	{
		'title': 'Red Book Title',
		'publisher_id': 1,
		'pages_num': 200,
		'cover_image': 'Red Cover'
	},
	{
		'title': 'Blue Book Title',
		'publisher_id': 2,
		'pages_num': 150,
		'cover_image': 'Blue Cover'
	}
]

def home(request):
	context = {
		'books': Book.objects.all()
	}
	return render(request, 'books/books.html', context)

def publishers(request):
	return render(request, 'books/publishers.html', {'title': 'publishers list'})

def authors(request):
	return render(request, 'books/authors.html', {'title': 'list of authors'})


def about(request):
	return HttpResponse('<h1>About Library</h1>')
