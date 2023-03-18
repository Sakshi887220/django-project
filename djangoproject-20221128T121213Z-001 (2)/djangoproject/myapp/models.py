from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class myModel(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
	last_modified = models.DateTimeField(auto_now_add = True)
	img = models.ImageField(upload_to = "images/")

	def __str__(self):
		return self.title

class Phone(models.Model):
	phone_no = models.CharField(max_length=10)
	user_id = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.phone_no

class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Employee(models.Model):
	name=models.CharField(max_length=124)
	age=models.IntegerField()
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

		