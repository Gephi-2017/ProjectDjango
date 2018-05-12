from django import forms
from .models import Person

# our new form
class PersonForm(forms.ModelForm):
    class Meta:
	model = Person
	fields = ('Name', 'Email',)
    
