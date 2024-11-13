

## USER AUTHENTCIATION

## NOW AS WE KNOW AFTER USER REGISTRATION, WE HAVE TO ADD FUNCTIONALITY TO LOGIN/AUTHENTICATE A USER

## SO FIRST OF ALL AS WE KNOW WE HEAD TO FORMS.PY TO CREATE THE USER AUTHENTCIATION FORM FOR LOGGING IN AND WITH THAT 
## FOR WE KNOW WE HAVE CUSTOM DJANGO FORM, WHERE WE DECLARE THE FIELDS OURSELVES   (EVERYTHING EXPLAINED IN PROJECT)



####################  FORMS.PY

## BELOW WE CREATE THE LoginForm for authentication

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  #we import this AuthenticationForm for authenticating our user forms
from django.contrib.auth.models import User

from django import forms  ##we import forms to create custom login forms
from django.forms.widgets import TextInput, PasswordInput 

## here we create the login form for authentciation
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

## ALL THE ABOVE IS DEFINED IN THE ELEVATE PROJECT (IN DEV FOLDER)


#### NOW AFTER MAKING A FORM FOR AUTHENTICATION, WE WILL MOVE ONTO VIEWS.PY FILE AND EDIT THE my-login VIEWS FUNCTIONS




#####################  VIEWS.PY FILE

from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm  ##importing the LoginForm that we created in forms.py


## IMPORT THE TOOLS FOR AUTHENTCIATION OF USER

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):

    return render(request, 'journal/index.html')


#register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('my-login')

    context = {'RegistrationForm': form}

    return render(request, 'journal/register.html', context)


#login user
def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect ('dashboard')

    
    context = {'LoginForm' : form}

    return render(request, 'journal/my-login.html', context)




def dashboard(request):

    return render(request, 'journal/dashboard.html')



## NOW AFTER ETTING UP THE VIEWS.PY FILE FOR my-login FUNCTION, WE HAVE TO EDIT THE my-login TEMPLATE AS WELL, IT WILL BE SIMILAR TO REGISTER.HTML
## JUST WITH SOME MINOR CHANGES ACCORDING TO THE VIEW FUNCTION


################ my-login.html

# <html>

#     <head>

#         <title> Edenthought | Login </title>

#     </head>


#     <div class = "container">   <!-- we will have our form within this container -->


#         <h2> Login to your acount </h2>

#         <br>
#         <br>

#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ LoginForm.as_p }}   ##CHANGE THIS AND SOME TEXT ABOVE


#             <br> <br>

#             <button type = "submit"> &nbsp; Login </button>

#         </form>


### ALSO REMEBER TO ADD IN THE HREF LINK TO LOGIN BUTTON IN THE INDEX.HTML, SO THE LOGIN BUTTONS OF HOMEPAGE ARE RESPONSIVE AND REDIRECTS
### TO REGISTER PAGE ---{% url 'my-login' %}

