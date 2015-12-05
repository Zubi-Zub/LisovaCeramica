from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm): # data that are presented in the 'Change sign up'
	class Meta:
		model = SignUp
		fields = ['email', 'first_name', 'last_name']
		# excludes particular fields
		# exclude = []	

	# validating an email (the same can be provided for the first_name, last_name etc.)
	def clean_email(self):

		# print email into the terminal
		# print(self.cleaned_data.get('email'))

		email = self.cleaned_data.get('email') 

		# split email onto 2 parts: email_base (before '@') and email_provider (after '@')
		email_base, email_provider = email.split('@')

		# split email_provider onto 2 parts: domain (before '.') and email_extension (after '.')
		email_domain, email_extension = email_provider.split('.')

		if not email_extension == 'edu':
			raise forms.ValidationError('Please use a valid .EDU email address')

		return email