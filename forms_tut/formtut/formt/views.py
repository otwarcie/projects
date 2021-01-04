from annoying.functions import get_object_or_None
from django.shortcuts import render

from .models import Meal
from .forms import MealForm

def edit_meal(request, meal_id):
	meal = get_object_or_None(Meal, pk=meal_id)
	if not meal:
		# error handle
	if request.method == "POST":
		form = MealForm(request.POST, instance=meal, organizer=request.user)
		if form.is_valid():
			meal = form.save()
			# maybe add a success message for user
	else:
		form = MealForm(instance=meal, organizer=request.user)

	context = {
		'form': form,
		'meal': meal
	}
	return render('<template>')

