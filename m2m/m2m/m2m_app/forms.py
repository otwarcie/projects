from django.forms import ModelForm
from .models import Student, Course, Enrollment
from django.utils import timezone

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['name']

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['name']

class StudentEnrollForm(ModelForm):
	class Meta:
		model = Enrollment
		fields = ['student', 'date_enrolled', 'final_grade']
	def __init__(self, course_pk, *args, **kwargs):
		super(StudentEnrollForm, self).__init__(*args, **kwargs)

		enrolled = Enrollment.objects.filter(course=course_pk)
		self.fields['student'].queryset = Student.objects.exclude(id__in=enrolled)
		self.fields['date_enrolled'].initial = timezone.now()
