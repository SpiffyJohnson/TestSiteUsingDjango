from django.db import models

# Create your models here.
class Student(models.Model):
	cNumber 	= models.CharField(primary_key=True, max_length=10)
	firstName 	= models.CharField(max_length=100)
	lastName 	= models.CharField(max_length=100)
	major		= models.CharField(max_length=100)
	dob 		= models.DateField()
	gpa 		= models.FloatField()

	def __str__(self):
		return (self.lastName + ', ' + self.firstName)