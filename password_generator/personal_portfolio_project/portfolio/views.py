from django.shortcuts import render
from .models import Project

def home(request):
	title = 'one day, this will be my portfolio'
	some_text = 'some text here'

	projects = Project.objects.all()
	return render(request, 'portfolio/home.html', {'title': title, 'some_text': some_text, 'projects':projects})
