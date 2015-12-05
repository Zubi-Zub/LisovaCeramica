from django.db import models
from datetime import datetime

# Create your models here.
class SignUp(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20, blank=True)
	email = models.EmailField()
	created = models.DateTimeField(default=datetime.now)
	updated = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.email #returns email in 'Sign up'