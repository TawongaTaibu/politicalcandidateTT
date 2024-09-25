from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#This form enables a user to register as a member of the political party
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    id_number = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=30, required=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=gender_choices, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'surname', 'email', 'id_number', 'gender', 'username','password1', 'password2']
