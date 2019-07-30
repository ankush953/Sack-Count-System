from django import forms
from .models import SiteUser
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = [
            'First_name',
            'middlename',
            'Last_name',
            'Email_address',
            'profile_pic',
            'address',
        ]

class BasicForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	Confirm_password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = [
			'username',
		]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = [
            'First_name',
            'middlename',
            'Last_name',
            'Email_address',
            'profile_pic',
            'address',
        ]


class LogInForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
