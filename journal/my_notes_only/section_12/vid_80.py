

####  INTEGRATING FLASH MESSAGES

## FLASH MESSAGES ARE ESSENTIALLY NOTIFICATION MESSAGES, THAT WE CAN UTILIZE IN OUR DJANGO APPLICATIONS AND IN ORDER TO USE THESE NOTIFICATIONS
## OR FLASH MESSAGES, WE NEED TO MAKE USE OF DJANGO MESSAGES

## WE WILL START OUR CHANGES WITH VIEWS.PY FILE

##################  VIEWS.PY FILE

from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm  


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required  


## FIRST OF ALL WE WILL IMPORT THE MESSAGES LIBRARY
from django.contrib import messages

## NOW WE WILL SET UP OUR MESSAGES IN THE CORROSPONDING VIEW, WE WILL DO IT WITH THE REGISTER VIEW





def homepage(request):

    return render(request, 'journal/index.html')


#register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            ## JUST HERE AFTER THE FORM IS VALIDATED AND ALL SAVED 
            messages.success(request, "User created")

## detail of above line

# messages.success(): This is a function provided by Django to display success messages to the user. It's used to inform the user about successful operations, like successfully creating a new account.
# request: The request parameter represents the HTTP request made by the user's browser. It's passed to the function to associate the message with the current request. This ensures that the message is displayed to the user in the appropriate context.
# "User created": This is the actual message that will be displayed to the user. It's a string that describes what action was successfully completed. In this case, it tells the user that their account has been successfully created.
# In simple terms, messages.success(request, "User created") is like telling Django to show a little message to the user saying, "Hey, your account was created successfully!" It's a nice way to give feedback to the user after they've completed an action on the website.

###  WHY WE USE THE REQUEST PARAMETER

# The request parameter represents the HTTP request made by the user's browser. It's passed to the function to associate the message with the current request. This ensures that the message is displayed to the user in the appropriate context.
# In summary, the request parameter is necessary for Django's messaging framework to store and display messages in a way that's consistent, contextual, and flexible across different parts of the application.

## SEE WE WANT THIS MESSAGE TO BE SHOWN ON THE PAGE THAT WE ARE REDIRECTING TO AND THAT IS THE my-login PAGE,SO WE NEED TO SET UP IN OUR TEMPLATES THE STRUCTURE TO LOOP OUT THE SUCCESS MESSAGE
## AND THEN WE WANT TO OUTPUT THE MESSAGE ON my-login PAGE. 
## SEE THIS MESSAGE THING, WE USUALLY USE IT WHERE WE  DO THINGS LIKE REGISTERING A USER, LOGIN IN OR VERIFYING SOMETHING AND AS ITS A SUCCESS MESSAGE, AND WE HAVE REDIRECT BELOW THIS
## SO THIS MESAGE WILL BE DISPLAYED ON THE REDIRECTED PAGE I.E my-login,SO if you use messages.success(), the success message will be displayed on the redirected page,
## AND WE EDIT THE my-login.HTML FOR THIS, NOT THE REGISTER.HTML, BECAUSE ITS GOING TO BE DISPLAYED ON MY-LOGIN.HTML. AFTER ALL THIS, LIKE WRITING THIS ALL AND ALSO EDITING THE HTML
## WHEN WE WILL BE DIRECTED TO MY-LOGIN.HTML, WE WILL AT THE TOP A NOTIFICATION MESSAGE, THAT SAYS, User created. 

###  NOW OVER TO my-login.html

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



###################### my-login.html

##  AS WE HAVE TO EDIT THIS FILE FOR THE MESSAGES, WE WILL INCORPORATE THESE CHANGES AT THE START OF OUR FORM TAG BELOW

# {% load static %}

# {% load crispy_forms_tags %}

# <html>

#     <head>

#         <title> Edenthought | Login </title>

#         <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/morph/bootstrap.min.css">


#         <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">

#     </head>

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">
 

#         <h2> Login to your acount </h2>

#         <br>
#         <br>

#         ####### RIGHT HERE WE NEED TO RENDER OUR MESSAGE, WE WILL BE USING A FOR LOOP FOR THIS. THE REASON WE ARE ADDING A FOR LOOP IS
#         ####### BECAUSE WE CAN HAVE SEVERAL MESSAGES SET UP( FOR NOW ITS ONLY ONE). SEE WE ALSO HAVE LEVELS FOR THESE MESSAGES, messsages.success
#         ####### IS CONSIDERED ONE AND message.error is CONSIDERED OTHER LEVEL(WE CAN HAVE MANY LEVELS/ MESSAGE TYPES), SO TO DIFFERENTIATE BETWEEN THESE 
#         ####### LEVELS, WE USE IF STATEMENT INSIDE THE FOR LOOP 

          ### ALSO REMEMBER THE MESSAGE DISPLAYED ON MY-LOGIN PAGE(IF WE LET BE LIKE THIS), WILL BE THERE TILL YOU AGAIN REFRESH THE LOGIN PAGE
          ### SO WE DONT WANT THAT TO HAPPEN AND WE WANT LIKE AFTER 5-6 SECODNS THE MESSAGE SHOULD DISAPPEAR ITSELF, SO WE IMPORT A CUSTOM
          ### CREATED JS FILE, WHICH HAS SET TIMEOUT FUNCTION, WHICH TAKES IN THE ID OF OF THIS MESSAGE BY GET METHOD AND THEN SETS A TIMEOUT
          ### AND AFTER THAT TIME IS OVER, MESSAGE DISAPPEARS, THIS KIND OF PUTS IN A NOTIFICATION EFFECT, THE CUSTOM JS FILE IS IMPORTED BELOW
          ### UNDER SCRIPT TAG

#         {% for message in messages %}

#             {% if message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}   # so if the message type is message.success, return the message that was
#                                                                        # written in the view function with messages.success function, SEE WE CAN
                                                                         # HAVE message.error (or any other message type) in the same view function as this
                                                                         # so to differentiate we use if statement with type of message

#                 <p id="message-timer"  class="alert alert-primary float-center text-center message-text"> {{message}} </p>   ## added some styling, thats it
                                                                                                           ## message-text is the text color imported from css file
                                                                                                           ## message-timer is the id which is used in Js file to get the message element
#             {% endif %}


#         {% endfor %}

#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ LoginForm|crispy }}


#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Login </button>

#         </form>

#     </div>

#     <br>

#### HERE WE WILL IMPORT THE CUSTOM JS FILE FROM STATIC

#      <script src="{% static 'js/app.js' %}"></script>


# </html>

######## SO AFTER THIS YOU WILL SEE A MESSAGE USER CREATED ON MY-LOGIN PAGE