from django import forms
from django.forms import fields, CheckboxInput

class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		fields = ('time', 'location')

	def __init__(self, *args, *kwargs):
		self.organizer = kwargs.pop('organizer')
		super(MealForm, self).__init__(*args, *kwargs)
		if not self.instance:
			self.fields['location'].initial = self.organizer.default_location
		self.fields['required'].widget = CheckboxInput(required=False)
		# do stuff with the time to put it in UTC based on the user's default timezone and data passed into the form.

	def clean_time(self):
		time = self.cleaned_data['time']

	def save(self, *args, *kwargs):
		self.instance.organizer = self.organizer
		meal = super(MealForm, self).save(*args, *kwargs)
		return meal
