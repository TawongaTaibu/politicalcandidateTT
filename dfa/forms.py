from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    """
    A form for creating a new user as a member of the political party.

    This form inherits from Django's UserCreationForm and adds additional
    fields specific to the political party registration.

    Attributes:
        first_name (str): The first name of the user.
        surname (str): The surname of the user.
        email (str): The email address of the user.
        id_number (str): The identification number of the user.
        username (str): The username for the user account.
        gender (str): The gender of the user, selected from predefined choices.
    """

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
        fields = ['first_name', 'surname', 'email', 'id_number', 'gender', 'username', 'password1', 'password2']
        """
        Meta class to define additional properties for the CreateUserForm.

        Attributes:
            model (User): The model associated with this form.
            fields (list): List of field names that will be included in the form.
        """
