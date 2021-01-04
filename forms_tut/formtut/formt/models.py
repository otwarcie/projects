from django.conf import settings
form django.db import models


class Meal(models.Model):
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='organizer')
	time = models.DateTimeField(null=True, blank=True)
	location = models.CharField(max_length=100)
	required = models.NullBooleanField(default=None)


