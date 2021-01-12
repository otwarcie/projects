from django.shortcuts import render, redirect, get_object_or_404
# from django.forms import ModelForm
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, StudentEnrollForm

def courses_list(request):
	return render(request, 'm2m_app/courses_list.html', {'courses': Course.objects.all()})

def students_list(request):
	return render(request, 'm2m_app/students_list.html', {'students': Student.objects.all()})

def student_add(request):
	if request.method == 'GET':
		return render(request, 'm2m_app/student_add.html', {'form':StudentForm()})

	try:
		form = StudentForm(request.POST)
		form.save()
		return redirect('students_list')
	except ValueError:
		return render(request, 'm2m_app/student_add.html', {'form':StudentForm(), 'error': 'Bad data, try again.'})

def student_enroll(request, course_pk):
	the_course = get_object_or_404(Course, pk=course_pk)

	if request.method == 'GET':
		return render(request, 'm2m_app/course_add_student.html', {'form':StudentEnrollForm(course_pk=course_pk), 'course_name': the_course.name})

	form = StudentEnrollForm(course_pk, request.POST)
	newstudent = form.save(commit=False)
	newstudent.course = Course.objects.get(pk=course_pk)
	newstudent.save()

	return render(request, 'm2m_app/courses_list.html', {'courses': Course.objects.all()})

def course_add(request):
	if request.method == 'GET':
		return render(request, 'm2m_app/course_add.html', {'form':CourseForm()})

	try:
		form = CourseForm(request.POST)
		form.save()
		return redirect('courses_list')
	except ValueError:
		return render(request, 'm2m_app/course_add.html', {'form':CourseForm(), 'error': 'Bad data, try again.'})

def course_enroll(request, student_pk):
	return render(request, 'm2m_app/student_detail.html')

def student_detail(request, student_pk):
	the_student = get_object_or_404(Student, pk=student_pk)
	courses = the_student.course_set.all()

	enrolls = []
	for c in courses:
		enrolls.append([(f'{e.course.name}, {e.date_enrolled}, {e.final_grade}') 
			for e in Enrollment.objects.all() if e.student == the_student and e.course == c])
	return render(request, 'm2m_app/student_detail.html', {'student': the_student, 'courses': courses, 'enrolls': enrolls})

def course_detail(request, course_pk):
	the_course = get_object_or_404(Course, pk=course_pk)
	students = Student.objects.filter(course=the_course)

	enrolls = []
	for s in students:
		enrolls.append([(f'{e.student.name}, {e.date_enrolled}, {e.final_grade}') 
			for e in Enrollment.objects.all() if e.course == the_course and e.student == s])
	return render(request, 'm2m_app/course_detail.html', {'course': the_course, 'students': students, 'enrolls': enrolls})



	# moj_napis = f"Super napis {a} i mam tez {b}"