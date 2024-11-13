
####### SENDING WELCOME EMAILS

###  NOW LETS SAY FOR EXAMPLE YOU WANT TO SEND A NICE EMAIL TO YOUR USERS THAT HAVE SIGNED UP TO YOUR APPLICATION, THIS LECTURE IS FOR SETTING UP THAT FUNCTIONALITY

##E  WE WILL EDIT THE VIEWS.PY AND ADD IN A NEW VIEW FUNCTION  FOR THIS

################  VIEWS.PY


from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm, ThoughtForm, UpdateUserForm, UpdateProfileForm  


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required  



from django.contrib import messages


from .models import Thought, User, Profile

from django.core.mail import send_mail
#This import allows you to send emails from your Django application. send_mail is a function provided by Django
#that makes it easy to send emails without needing to deal with the complexities of email protocols directly.

from django.conf import settings
#This import gives you access to the settings of your Django project. Settings are configurations that control how your Django project behaves. By importing settings,
# you can access things like database configuration, security settings, and more, which are defined in your project's settings file.
## WE WILL USE THE SETTING TO IMPORT OUR HOST EMAIL FROM IT, THAT IS USED BY DJANGO BY TO SEND EMAILS LIKE WELCOME EMAILS AND ALSO PASSWORD RESET EMAILS AS WELL
## AS WE WE WANT THE WELCOME EMAIL TO BE SENT ONLY, WHEN A NEW USER REGISTERS, SO WE WILL WORK WITH register VIEW FUNCTION TO INCROPORATE THIS FUNCTIONALITY




# register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False) 

            form.save() 

            ## SO WE WILL ADD THE WELCOME MAIL SENDING FUNCTIONALITY HERE, AS WE FORM HAS BEEN SAVED, MEANS THE DATA WAS VALID AND USER WAS REGISTERED SUCCESSFULLY
            ## SO AFTER SUCCESSFUL REGISTRATION, WE WANT TO SEND THE WELCOME MESSAGE

            send_mail("Welcome to Edenthought!","Congratulation on creating your acount", settings.DEFAULT_FROM_EMAIL, [current_user.email])  

            ## SEE THE ABOVE FIRST WE USED THE send_mail WHICH IS IMPORTED ABVOE, THEN WE HAVE FOUR PARAMETRS DEFINED IN IT

            # 1-- FIRST THE SUBJECT OF THE MAIL
            # 2-- SECOND IS THE MESSAGE THAT WE WANT THE USER TO SEE
            # 3-- 3RD IS ADDING THE FROM/SENDER MAIL WHICH WILL ACTUALLY SEND THE MESSAGE AND THAT IS DEFAULT MAIL THAT WE HAVE PROVIDED UNDER DEFAULT_FROM_EMAIL
            #     IN SETTINGS.PY, WHICH DJANGO IS NOW USING BY DEFAULT TO ACTUALLY SEND THE MAIL
            # 4-- 4TH IS WHERE WE ENTER THE EMAIL OF RECEIVER/USER WHO RESGITERED. JUST GRAB THE CURRENT_USER WHICH THE USER JUST CREATED WITH THE DATA 
            #     AND WE GRAB .EMAIL FROM THAT DATA AND NOW EMAIL WILL BE SENT TO THAT PARTICULAR MAIL WITH WHICH THE USER REGISTERES

            ## SO IN SHORT This line of code will send an email with the subject "Welcome to Edenthought!" and the message "Congratulations on creating your account"
            ## to the email address of the current user. The email will be sent from the default email address configured in the Django project settings.


            profile = Profile.objects.create(user=current_user) 
       
            messages.success(request, "User created")

            return redirect('my-login')

    context = {'RegistrationForm': form}

    return render(request, 'journal/register.html', context)



##  NOW YOU WILL GET AN WELCOME EMAIL ON THE EMAIL THAT YOU HAVE USE WHILE REGISTERING A NEW USER

 