from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=30)
	students = models.ManyToManyField(Student, through='Enrollment')#, related_name='courses')

	def __str__(self):
		return self.name

class Enrollment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)#, related_name='membership')
	course = models.ForeignKey(Course, on_delete=models.CASCADE)#, related_name='membership')
	date_enrolled = models.DateField()
	final_grade = models.CharField(max_length=1, blank=True, null=True)

	class Meta:
		unique_together = [['student', 'course']]

	def __str__(self):
		return str(self.student)




