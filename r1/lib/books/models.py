from django.db import models
#from django.utils import timezone
#from django.contrib import admin


class Publisher(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return f'Wydawnictwo {self.name}'

class Author(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
#	birthdate = models.DateTimeField()

	def __str__(self):
		return f'{self.firstname} {self.lastname}, aka {self.nickname}'

class Book(models.Model):
	title = models.CharField(max_length=150)
#	author = models.ManyToManyField(Author, through='WrittenBy')
	author = models.ManyToManyField(Author)
	pages_num = models.IntegerField()
	publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
	cover_image = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.title}, {self.pages_num} str.'
'''
class WrittenBy(models.Model):
	book = models.ForeignKey(BookT, on_delete=models.PROTECT)
	author = models.ForeignKey(AuthorT, on_delete=models.PROTECT)
'''

'''
#*** nastepne 4 klasy z pytania na stackoverflow:
class Product(models.Model):
    group = models.CharField(max_length = 200, blank = False)
    mark = models.CharField(max_length = 200, blank = True)
    points = models.IntegerField(blank = False)

class ProductTabular(admin.TabularInline):
    model = Invoice.product.through

class Invoice(models.Model):
    price = models.FloatField(blank=False, default=10.0)
#    file = models.FileField(blank=False)
    product = models.ManyToManyField(Product, through='Sold')
    date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

class Sold(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
'''
