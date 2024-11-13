
### Create a Thought- [CREATE]- Part 1 and Part 2

## WE KNOW IN ORDER TO CREATE and  UPDATE  THE THOUGHT, WE NEED TO TO HAVE MODEL FORM FOR THAT, SO WE WILL HEAD ONTO
## FORMS.PY AND CREATE A FORM FOR THE Thought Model.

################### FORMS.PY


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import TextInput, PasswordInput 


# THIS PART IS ADDED AND THE BELOW THOUGHT FORM

from django.forms import ModelForm  ## import ModelForm for converting the thought model to form
from .models import Thought   ## we import the Thought model/database


## NOW create form for theThought model
class ThoughtForm(ModelForm):

    class Meta:

        model = Thought
        fields = ['title', 'content',] ## see we dont use '__all__' because we have relationship field(i.e user field) in this model
                                               ## and we dont want it to be visible on Web Page to the USER, so we dont add it in here





## not working on theses
# class LoginForm(AuthenticationForm):

#     username = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())


# class CreateUserForm(UserCreationForm):

#     class Meta:

#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


### NOW AFTER CREATING A FORM FOR OUR THOUGHT MODEL, WE WILL GO ONTO VIEWS.PY FILE TO DISPLAY THE FORM AND ALSO TO HAVE SOME FUNCTIONALITY TO
### ENTER DATA IN THE FORM. WE DONT HAVE A VIEW FUNCTION FOR CREATING THOUGHTS, SO WE WILL HAVE A NEW VIEW FUNCTION FOR CREATE OPERATIONS AND 
### DONT FORGET TO ADD THE URL FOR IT. WE ALSO CREATE A html template for this view function called create-thought.html, which we will edit
### later below

################## VIEWS.PY FILE   (create_thought--name of view function, that we create and edit in this lecture)



from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm, ThoughtForm ## HERE WE IMPORT THE THOUGHT FORM  


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required  



from django.contrib import messages





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
@login_required(login_url='my-login') ## WE ADD THIS LOGIN DECORATOR HERE AS WELL, AS THOUGHT ARE CREATED AFTER LOGGIN IN AND NOBODY SHOULD HAVE ACCESS WITHOUT LOGGING IN
def create_thought(request):

    form = ThoughtForm()

    if request.method == 'POST':

        form = ThoughtForm(request.POST)

        if form.is_valid:   ## SEE AFTER THIS WE USED TO JUST SAVE THE FORM LIKE THIS form.save() and details in form were saved to database, BUT AS WE REMEMBER WE HAVE A FOREIGN KEY
                            ## ASSOCIATED WITH THIS FORM(Thought_form, basically the model of thoughtform is associated to User model by a foregin key AND user IS THE NAME OF VARIABLE
                            ## THAT DEFINES THIS RELATIONSHIP IN MODELS.PY(thought model) THROUGH A FOREIGN KEY) 
                            ## SO WHAT WE NEED TO DO IS THEN WHEN A USER IS LOGGED IN AND AS HE FILLS THE DATA IN FORM(ThoughForm) AND SUBMITS THE POST REQUEST, WE NEED TO MAKE
                            ## SURE THAT WE ATTACH THAT USER TO THAT OBJECT THAT HE CREATES. NOW WE WILL DO THE BELOW

            thought = form.save(commit=False) ## SEE AFTER FILLING THE FORM AND SUBMITTING THE POST REQUEST, WE ARE BASICALLY TELLING DJANGO, HEY I WANT YOU TO POST THIS INFORMATION
                                              ## I.E THE DATA ENTERED IN THE FIELDS TO DATABASE, BUT BUT I JUST WANT YOU TO WAIT A MOMEMNT BECAUSE WE WANT TO GO AHEAD AND ADD SOMETHING
                                              ## EXTRA TO OUR FORM, ESPECIALLY IN TERMS OF user FIELD IN MODELS.PY(user IS THE NAME OF VARIABLE THAT DEFINES THIS RELATIONSHIP IN MODELS.PY THROUGH A FOREIGN KEY)
                                              ## SO  AS WE HAVE user FIELD IN MODELS.PY(Thought model) AND THAT FIELD WE KNOW HAS TO BE ASSIGNED A VALUE. SO THAT IS WHAT WE WILL BE DOING BELOW,
                                              ## THAT IS ASSIGNING A VALUE TO THE user ATTRIBUTE, SO IT HAS A REFERENCE TO THAT ASSIGNED VALUE. IN SHORT HERE WE ARE JUST GRABBING THE SAVED OBJECT AND THEN BELOW
                                              ## ACCESSING THE USER COLUMNOF THAT OBJECT AND ASSIGINING IT TO CURRENT USER
                                              ## if you don't use commit=False and try to assign the user field afterward, you will encounter an error because the form is immediately saved to the database, and 
                                              ## Django expects all required fields, including the foreign key (user), to be present at the time of saving. means if the form is saved here, it will be saved without
                                              ## Users infor and that would raise an error

            thought.user = request.user       ## thought.user MEANS, THAT WE ARE LOOKING FOR THIS SPECIFIC FIELD IN THE FORM(AS user was a attribute in Thought model and then converted to form),As form is
                                              ## saved with thought variable and we are in that form looking for the user field which is nothing but a relationship field or reference field
                                              ## AND NOW AS WE HAVE TH FIELD LOOKED UP BY USING thought.user, WE WILL ASSIGN A VALUE TO THIS user FIELD AND THAT WOULD request.user
                                              ## SO ESSENTIALLY WHAT WE ARE DOING IS WE ARE ASSIGNING THE VALUE OF THIS user FIELD/ATTRIBUTE BASED ON THE REQUEST THAT IS BEING MADE. SO IN SHORT, WHOEVER
                                              ## USER IS LOGGED IN AND MAKING THIS POST REQUEST(THAT IS SUBMITTING THE FORM), THAT USER WOULD BE REFERENCED TO THIS user FIELD/ATTRBUTE 
                                              ## AND THE THOUGHT CREATED(DATA SUBMITTED IN FORM) WOULD BE ASSIGNED TO THAT USER WHO WAS LOGGED IN AND WHO CREATED THE THOUGHT
                                              ## request.user refers to the currently logged-in user in a Django view. When a user logs into your Django application, Django stores information about that
                                              ## user's session, including their authentication status and user details.
                                              ## SO INSHORT BY ABOVE WE MEAN, THAT GET THE user FIEld FROM THE FORM(FORM IS SAVED IN thougth variable i.e why thought.user) AND WE ASSIGN IT TO THE
                                              ## USER WHOS LOGGED IN OR WHOSOEVER SUBMITTED THE POST REQUEST(FILLED IN THE DAT IN THE FORM)
                                              # NOW WE WILL SAVE THE FORM

            thought.save()    ## saved to database

            return redirect('dashboard')

    context = {'CreateThoughtForm':form}        

    return render(request, 'journal/create-thought.html', context)


#### NOW HEAD ONTO  create-thought.html TO EDIT IT

#########################   create-thought.html

### SE AS WE HAVE A FORM TO SUBMIT AND ALSO WE NEED TO HAVE THE EXTENDED NAVBAR, WE CN JUST COPY CONTENTS FROM dashboard.html and my-login.html
### AND THEN JUST EDIT AS PER OUR REQUIREMENTS FOR create_thought view function

## SEE ADD EXTEND AND BLOCK CPABALITIES FROM DASHBOARD.HTML AND FORM THAT WE HAVE TO SUBMIT FROM my-login.html and thats it

# {% extends 'journal/navbar.html' %}  

# {% load crispy_forms_tags %}


# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">
#         <h3> Create a thought</h3>

#         <br>
#         <br>
#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ CreateThoughtForm|crispy }}   ##### PASS IN THE KEY HERE


#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Create </button>

#         </form>

#     </div>

#     <br>
# {% endblock %}   



###  ALSO AS YOU HAVE NOW CREATD A create_thought VIEW FUNCTION, JUST IN THE NAVBAR.html FILL IN THE HREF LINK FOR CREATE THOUGH SO ON CLICKING 
###  CREATE THOUGHT ON NAVBAR(ON DASHBOARD), WE ARE REDIRECTED TO PAGE, WHERE WE CAN CREATE A THOUGHT




