from django import forms
from adobe_app.models import Address, User 
# class FormName(forms.Form):
# 	name = forms.CharField()
# 	email = forms.EmailField()
# 	text = forms.CharField(widget=forms.Textarea)



class MyNewForm(forms.ModelForm):
	class Meta():
		model = Address
		fields = "__all__"

class NewUserForm(forms.ModelForm):
	class Meta():
		model = User
		fields = "__all__"
