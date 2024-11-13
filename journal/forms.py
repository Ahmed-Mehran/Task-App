


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import TextInput, PasswordInput 

from django.forms import ModelForm  

from .models import Thought, Profile ## WE IMPORT THE PROFILE MODEL, SO THAT WE CAN CONVERT IT INTO FORM



class ThoughtForm(ModelForm):

    class Meta:

        model = Thought
        fields = ['title', 'content']

########################

## USER FORMS

## FORM FOR CREATING THE USER
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


## FORM FOR LOGGIN IN THE USER
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



## FORM FOR UPDATING THE USER
class UpdateUserForm(ModelForm): 

    password = None 

    class Meta:

        model = User
        fields = ['username', 'email',]  
        exclude = ['password1', 'password2',] 



## FORM FOR UPLOADING PROFILE IMAGE
class UpdateProfileForm(ModelForm):  ## or forms.ModelForm

    profile_pic = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:

        model = Profile
        fields = ['profile_pic']  