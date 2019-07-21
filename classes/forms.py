from django import forms
from .models import Classroom, Student
from django.contrib.auth.models import User


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class SignupForm(forms.Form):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email' ,'password']
		widgets={
        'password': forms.PasswordInput(),
        }

class StudentForm(forms.Form):
	class Meta:
		model = Student
		fields = ['name', 'date_of_birth', 'gender', 'exam_grade', 'classroom']