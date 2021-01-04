from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	date_posted = models.DateField(blank=True, null=True)
	description = models.TextField()

	def __str__(self):
		return self.title

