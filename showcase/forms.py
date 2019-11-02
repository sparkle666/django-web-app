from django import forms
from .models import Design, DesignCategory

class DesignForm(forms.ModelForm):
	class Meta:
		model = Design
		exclude = ['likes', 'created_on', 'updated_on']
		widgets = {
			"name": forms.TextInput(attrs={"class": "w3-input w3-border w3-round"}),
			"image": forms.ClearableFileInput(attrs={"class": "w3-border w3-round"}),
			"design_category": forms.Select(attrs={"class": "w3-select w3-round w3-border"}),
			"date_added": forms.DateTimeInput(attrs={"class": "w3-input w3-border w3-round", "placeholder": "dd/mm/yy"}),				
		}
		
class DesignCategoryForm(forms.ModelForm):
	class Meta:
		model = DesignCategory
		fields = "__all__"
		widgets = {
			"name": forms.TextInput(attrs={"class": "w3-input w3-border w3-round"}),
			"description": forms.Textarea(attrs={"class": "w3-input w3-border w3-round"}),	
		}

class LoginForm(forms.Form):
	username = forms.CharField(max_length=200, widget = forms.TextInput(attrs={"class": "w3-input w3-border w3-round"}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {"class": "w3-input w3-round w3-border"}))