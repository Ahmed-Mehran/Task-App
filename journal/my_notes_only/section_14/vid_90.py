

########   PROFILE MANAGEMENT-- UPDATE OUR USERNAME AND EMAIL

## AS WE HAVE LEARNT TO CREATE/REGISTER A USER(WITH USERNAME AND EMAIL AND PASSWORD). NOW WE WILL LEARN HOW WE WILL UPDATE OUR USERNAME AND PASSWORD

### FIRST OF ALL WE WILL CREATE A VIEW FUNCTION FOR THIS, ALSO WE WILL CREATE A HTML FILE AND PUSH THE VIEW FUNCTION IN URL AS WELL
## ALSO IN THE NAVBAR.HTML, ADD IN A NEW LINK TO HAVE AN OPTION OF PROFILE MANAGEMENT ON NAVBAR

##### SEE WE REMEMBER WHEN WE REGISTERED A USER, WE FIRST CREATED A FORM(CreateUserForm) AND FOR LOGINNG IN THE USER AS WELL, WE IMPORTED SOME AUTHNTCIATION FUNCTION
##### AND CREATED A FORM FIRST. NOW FOR UPDATING THE USER WE WILL DO THE SAME, WE WILL CREATE A FORM AND THEN WE WILL EDIT THAT ACCORDINGLY


#############  FORMS.PY  (UpdateUserForm)





from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import TextInput, PasswordInput 

from django.forms import ModelForm  

from .models import Thought   



class ThoughtForm(ModelForm):

    class Meta:

        model = Thought
        fields = ['title', 'content']

########################

## USER FORMS


## FORM FOR CREATING THE USER
class CreateUserForm(UserCreationForm):# or forms.ModelForm--one and the same thing

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


## FORM FOR LOGGIN IN THE USER
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())






## FORM FOR UPDATING THE USER

## WHEN WE CREATED A FORM FOR REGISTERING USER(CreateUserForm), WE GOT A DEFAULT FORM(UserCreationForm) PROVIDED BY DJANGO AND THE MODEL THAT WE CHOSE WAS 
## ALSO A DEFAULT MODEL/DATABBASE TABLE PROVIDEDD BY DJANGO CALLED User model. NOW WE WILL AGAIN USE THIS User MODEL, AS WE WILL BE UPDATING THE FIELDS
## OF THIS USER MODEL ONLY, BUT WE WONT USE THE DEFAULT DJANGOF FORM(UserCreationForm) AS ITS ONLY USED FOR CREATING/REGISTERING NEW USERS
## ALSO ITS BETTER TO CREATE SEPARATE FORMS FOR USER FUNCTIONALITY BECAUSE using separate forms for user registration, login, and profile update enhances
## code organization, clarity, security, and flexibility, making the application easier to build, maintain, and scale.

## FORM FOR UPDATING THE USER
class UpdateUserForm(ModelForm):  # or forms.ModelForm--one and the same thing

    password = None  ## we wont be updating the password for now, we will do that in later upcomming lectures

    class Meta:

        model = User

        fields = ['username', 'email',]  ## we will only update username and email for now
        exclude = ['password1', 'password2',]  ## see this would ignore the passwords fields. but its not important to wirte this exclude statement
                                               ## as above in fields, we have not mentioned the password fields, but stiil to have better and cleaner
                                               ## code , we write it

#######  NOW WE WILL GO ONTO OUR VIEWS.PY FILE AND WRITE A NEW VIEW FUNCTION TO UPDATE THE USER FORM


################ VIEWS.PY   (profile_management---view function name)


from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm, ThoughtForm, UpdateUserForm  ## FIRST OF ALL WE WILL IMPORT THE UPDATE USER FORM


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required  



from django.contrib import messages


from .models import Thought, User  ## import the default User model provided by Django to run Querires to update the user





def homepage(request):

    return render(request, 'journal/index.html')


#register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

       
            messages.success(request, "User created")

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



#logout
def user_logout(request):

    auth.logout(request)

    return redirect('')


@login_required(login_url='my-login')
def dashboard(request):

    return render(request, 'journal/dashboard.html')




# CREATE
@login_required(login_url='my-login') 
def create_thought(request):

    form = ThoughtForm()

    if request.method == 'POST':

        form = ThoughtForm(request.POST)

        if form.is_valid:  

            thought = form.save(commit=False) 

            thought.user = request.user      

            thought.save()    

            return redirect('my-thoughts')

    context = {'CreateThoughtForm':form}        

    return render(request, 'journal/create-thought.html',context)

    
# READ
@login_required(login_url='my-login') 
def my_thoughts(request):



    current_user = request.user.id  

    thought = Thought.objects.all().filter(user=current_user)  

    context = {'AllThoughts': thought}

    return render(request, 'journal/my-thoughts.html', context)



# UPDATE
@login_required(login_url='my-login')    
def update_thought(request, pk): 

    thought = Thought.objects.get(id=pk, user=request.user)

    form = ThoughtForm(instance=thought)

    if request.method == 'POST':

        form = ThoughtForm(request.POST, instance=thought)
        
        if form.is_valid:

            form.save()

            return redirect('my-thoughts')

    context = {'UpdateThought':form}
    
    return render(request, 'journal/update-thought.html', context)




@login_required(login_url='my-login') 
def delete_thought(request, pk):

    thought = Thought.objects.get(id=pk, user=request.user)


    if request.method =='POST':

        thought.delete()

        return redirect('my-thoughts')


    return render(request, 'journal/delete-thought.html')



# UPDATE USER
@login_required(login_url='my-login') 
def profile_management(request):

    current_user = request.user.id

    user = User.objects.get(id=current_user)

    form  = UpdateUserForm(instance=user)

    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=user)

        if form.is_valid():

            form.save()

            return redirect('dashboard')


    context = {'ProfileForm':form}

    return render(request, 'journal/profile-management.html', context)

## WHAT WE HAVE DONE ABOVE IS SIMPLE AND IS VERY SIMILAR TO UPDATE(PART OF CRUD) OPERATION. FIRST WE GET THE ID OF THE CURRENTLY LOGGED IN USER
## THEM WE RUN A QUERY AND GET THE ACTUAL USER BY THAT ID AND THE WE PUT THE USER DETAILS IN THE FORM AND THEN SIMPLE UPDATE. A SIMPLE WAY OF WRITING THE
## ABOVE IS JUST SKIP THE FIRST TWO LINES I.E current_user = request.user.id AND user = User.objects.get(id=current_user) AND SIMPLY IN form wirte
## form = UpdateUserForm(instance=request.user). THIS WILL ALSO IMPORT THE USER LOGGED IN. THIS IS ALSO CORRECT AND ABVOE IS ALSOCORRECT. ABOVE IS DONE BY ME
## AND THIS ONE IS THE UDEMY METHOD


#### NOW WE WILL GO ONTO profile-management.html TO RENDER THE ABOVE VIEW FUNCTION


#########################  profile-management.html

##  WE WILL JUST COY FROM update-thought.html AND JUST CHANGE THE TEXT AND THE TEMPLATE INHERITANCE VARIABLE TO THE KEY VALUE OF profile_mananagement view function

# {% extends 'journal/navbar.html' %}  

# {% load crispy_forms_tags %}


# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">
#         <h3> Update Username & email</h3>

#         <br>
#         <br>
#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ ProfileForm |crispy }}



#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Update User </button>

#         </form>

#     </div>

#     <br>
# {% endblock %}   






#########  LINK THAT WE HAVE ADDED IN THE NAVBAR.HTML AND ALS THE URL PATH (NOT IMPORTANT, JUST RECORD FOR WHAT WE DID )

# <li class="nav-link">
        
#                     <a class="nav-link"  href="{% url 'profile-management' %}"> Pofile Management </a>
        
#                   </li>
        
        
#                   &nbsp;     &nbsp;     &nbsp;

##   URL PATH

# path('profile-management',views.profile_management,name='profile-management'),



## NOW YOU WILL BE ABLE TO UPDATE THE USER AND IT WILL REFLECT ON ADMIN DASHBOARD AS WELL

