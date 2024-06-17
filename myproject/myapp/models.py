from django.db import models

# Create your models here.
class Employee (models.Model):
	post_id=models.IntegerField()
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,blank=True)
	email = models.EmailField(unique=True)
	body=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.title