from django.db import models
from django.utils import timezone

class Author(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	birthdate = models.DateTimeField()

class Publisher(models.Model):
	name = models.CharField(max_length=50)

class Book(models.Model):
	title = models.CharField(max_length=100)
	pages_num = models.IntegerField()
	cover_image = models.ImageField()
#	author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
	publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class BookAuthor(models.Model):
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

