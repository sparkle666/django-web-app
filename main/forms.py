from django import forms
from .models import Person
class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = '__all__'

class ProfileForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=200)

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'w3-input'}))
	password= forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class': 'w3-input'}))
	