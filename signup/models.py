from django.db import models

# Create your models here.
class SignUp(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20, blank=True)
	email = models.EmailField()