

#####  CREATE A NEW USER

### SO AS WE WANT USERS TO BE ABLE TO REGISTE ON OUR WEBSITE, WE HAVE TO FIRST CREATE USER AND REGISTER IT


### SEE AS WE KNOW TO REGISTER USE WE HAVE TO CREATE A MODEL FORM AND USE THE DFAULT FORM CREATION METHODS PROVIDE BY DJANGO ((WE HAVE ALREADY 
### DONE THIS IN THE ELEVATE PROJECT ))

#################  FORMS.PY


### WE KNOW WE WILL FIRST IMPORT THE DFAULT UserCreation form, so we have the necesary form type for registering

from django.contrib.auth.forms import UserCreationForm

## NOW IMPORT THE DEAULT MODEL CLASS THAT IS User
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

## ALL THE ABOVE IS DEFINED IN THE ELEVATE PROJECT (IN DEV FOLDER)


### NOW WE WILL HEAD ON TO THE VIEWS.PY FILE TO REGISTER VIEW FUNCTION, WHERE WE WILL CREATE A RESPONSE FOR THIS FORM


##################  VIEWS.PY FILE



from django.shortcuts import render,redirect

from .forms import CreateUserForm   ### we import the form that we had created

# Create your views here.
def homepage(request):

    return render(request, 'journal/index.html')


# register
def register(request):   #here we have Created a register view to register User

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('my-login')

    context = {'RegistrationForm': form}

    return render(request, 'journal/register.html', context)

### NOW WE WILL EDIT THE REGISTER.HTML FILE FOR RENDERING OUT THE DATA



def my_login(request):

    return render(request, 'journal/my-login.html')


def dashboard(request):

    return render(request, 'journal/dashboard.html')



##########   REGISTER.HTML


# <html>

#     <head>

#         <title> Edenthought | Register </title>

#     </head>


#     <div class = "container">   <!-- we will have our form within this container -->


#         <h3> Create your account </h3>

#         <h5> share your thoughts today </h5>

#         <br>
#         <br>

#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ 'RegistrationForm'.as_p }}

#             <br> <br>

#             <button type = "submit"> &nbsp; Create Account </button>

#         </form>




#     </div>


# </html>

### ALSO REMEBER TO ADD IN THE HREF LINK TO REGISTER BUTTON IN THE INDEX.HTML, SO THE REGISTER BUTTONS OF HOMEPAGE ARE RESPONSIVE AND REDIRECTS
### TO REGISTER PAGE ---{% url 'register' %}

