from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'first_name', 'created', 'updated'] #display the list of fields shown in the admin site
	form = SignUpForm # use form in the 'Change Sign up'
	# class Meta:
	# 	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
