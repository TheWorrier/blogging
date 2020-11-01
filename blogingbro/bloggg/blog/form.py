from django import forms
from blog.models import Person

class PersonInfo(forms.ModelForm):
    class Meta:  
        model = Person
        fields = "__all__"



