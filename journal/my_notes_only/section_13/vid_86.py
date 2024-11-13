

####  READ A THOUGHT----  [READ]

### SO THIS IS THE READ PART OF THE CRUD OPERATIONS, AS WE HAVE DONE THE CREATE PART OF CRUD, WE NEED SOME FUNCTIONALITY TO READ AND IN THIS LECTURE
### WE WILL DO THAT, AND AS WE REMEMBER, WE SET UP DATABSE QUERIES IN ORDER TO GET THIS UP AND RUNNING AS WE DESIRE


## FIRST OF ALL, AS WE ARE CREATING A NEW FUNCTIONALITY OF READ, WE WILL CREATE A NEW FUNCTION TO READ AND ALSO DONT FORGET TO CONNECT THAT VIEW FUNCTION 
## IN THE URLS.PY


#####################   VIEWS.PY  (my_thoughts VIEW FUNCTION)

from django.contrib.auth.decorators import login_required  



from django.contrib import messages


from .models import Thought  ## IMPORT THIS, SO WE CAN USE IT FOR DATABASE QUERIES IN my_thought VIEW FUNCTION





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

            return redirect('my-thoughts')  ## AS NOW WE HAVE CREATED THE BELOW FUNCTION FOR VIEWING THOUGHTS, WE WOULD REDRIECT TO THAT AFTER
                                            ## CREATING A THOUGHT

    context = {'CreateThoughtForm':form}        

    return render(request, 'journal/create-thought.html',context)

    
# READ
@login_required(login_url='my-login') 
def my_thoughts(request):

    ## SO WE KNOW THAT, AS A USER IS LOGGED IN AND IF HE WANTS TO HAVE ACCESS OF THE THOUGHTS CREATED, THE THOUGHTS VISIBLE SHOULD BE THE ONE CREATED BY THE
    ## USER THAT IS LOGGED IN AND NOT ALL OTHER THOUGHTS CREATED BY OTHER USERS, MEANING USER SHOULD HAVE ACCESS ONLY TO THE THOUGHTS CREATE BY
    ## HIM. SO FIRST OF ALL WE WILL GRAB THE USER WHO IS LOGGEDE IN AND STORE IT IN A VARIABLE

    current_user = request.user.id  ## see now current_user has the id of logged in user, if we had done request.user only instead of request.user.id
                                    ## we would have only got the name and if you remember when we used to do database queries, we used to do it on id's
                                    ## because there can lot of same names in the databse, but id is unique
    
    ## NOW WE WILL CREATE A QUERY

    thought = Thought.objects.all().filter(user=current_user)  
## BY THE ABOVE WE MEAN THE FOLLOWING:

## Thought.objects.all(): This retrieves all objects (thoughts) from the Thought model in the database.
## THE FILTER PART BASICALLY CHECKS IN THE user ATTRIBUTE FIELD, WHICH IS THE RELATIONSHIP FIELD(and contains all id's  ofreference of referenced model(User)) AND
## CHECKS IF THE  current_user (WHICH HAS THE ID OF CURRENT LOGGED IN USER) IS EQUAL TO ANY id  IN THE user field of Thought model AND IF THERE IS STORE IT IN THE thought VARIABLE
## OR WE CAN SAY The filter() method checks the user attribute field, which is a relationship field (a ForeignKey) in the Thought model. It compares the current_user (which contains
## the ID of the currently logged-in user) with the IDs stored in the user field of the Thought model.
## If there are any thoughts where the user field matches the current_user ID, those thoughts are stored in the thought variable.
## The user=current_user part ensures that you're only retrieving thoughts associated with the current user. If current_user has an ID of, say, 1, then it will retrieve all thoughts
## where the user field is also 1 (meaning those thoughts were created by the current user).
# So, the entire line thought = Thought.objects.all().filter(user=current_user) basically says, "Give me all the thoughts, but only keep the ones that belong to the currently logged-in user."
# It's a way to fetch only the thoughts created by the logged-in user.
## BHAI SIMPLE HAI, YAI UPR LINE KEH RAHI HAI MEREKO SAARAI THOUGHT OBJECT LAAKAI DEDE AUR FIR FILTER KAR AISAI KI JO MERA CURRENT USER, AGAR USKI ID KISI B user ID SAI MILTI HAI
##(HAMAI PATA HAI user FIELD RELATIONSHIP FIELD HAI AUR USKAI PAAS SABH ID'S KA ACCESS HAI), TOH JO B ID MATCH KRAHI HAI USKA DATA THOUGHT VARIABLE MAI DAAL DAI.








    context = {'AllThoughts': thought}

    return render(request, 'journal/my-thoughts.html', context)


### NOW AS WE HAVE CREATED THE VIEW FUNCTION AND ALSO REGISTERED THE URL FOR THE VIEW FUNCTION, WE WILL NOW CREATE A NEW HTML TEMPLATE i.e my-thoughts.html TO RENDER THE WEBPAGE AND DISPLAY CONTENT

#########################   my-thoughts.html



########  WE CAN JUST COPY CONTENT FROM CREATE-THOUGHT.HTML AND EDIT IT ACORDINGLY



# {% extends 'journal/navbar.html' %}  


# {% block content %}

#     <h3> My Thoughts</h3>

#     <br>

#     ### WE JUST RUN A FOR LOOP TO DISPLAY ALL THE DATA RELATED TO THE USER AND AS WE WANT THE DATA TO BE INSIDE THE CONTAINER
#     ### WE HAVE THE CONTAINER CLASS INSIDE OF THE FOR LOOP

#     {% for thoughts in AllThoughts %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">

#             {{thoughts.title}}

#             <br>

#             {{thoughts.content}}

#             <br>

#             {{thoughts.date_posted}}

# #           <br>

#             {{thoughts.user}}  ### WE WILL UE THIS TO DISPLAY THE NAME OF USER WHO CREATED THE THOUGHT AND AS user IS THE FOREIGN KEY
##                               ### AND HAS THE NAME OF USER ASSOCIATED WITH THE THOUGHT, WE CAN USE THIS AND DISPLAY THE USER NAME
 
#     </div>

#     {% endfor %}

#     <br>
# {% endblock %}   


###  ALSO AS YOU HAVE NOW CREATD A my_thoughts VIEW FUNCTION, JUST IN THE NAVBAR FILL IN THE HREF LINK FOR VIEW THOUGHTS SO ON CLICKING 
###  VIEW THOUGHTS ON NAVBAR(ON DASHBOARD), WE ARE REDIRECTED TO PAGE, WHERE WE CAN VIEW THE THOUGHTS


### WE CAN ADD MORE VISIBILTY OF THE USER IN DASHBOARD.HTML, SO WHEN WE WILL LOGIN AND WE WILL BE DRIECTED TO OUR DASHBOARD, WE WOULD
### ALSO WANT TO VIEW THE PERSON/USER WHO IS LOGGED IN  AND WE CAN ADD THIS {{ user }} IN DASHBOARD.HTML TEMPLATE TO VIEW THE USER LOGGED IN ON DASHBOARD

########## dashboard.html

# {% extends 'journal/navbar.html' %}  



# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">

#         <h1> Dashboard</h1>   <h4>{{user}}</h4>    ### HERE YOU CAN SEE, DETAILS OF THIS IS BELOW

#         <br>
  

#         <a class="btn btn-outline-primary navbar-btn" type="button"  href="{% url 'user-logout' %}">logout Here</a>

#     </div>

# {% endblock %}    


# In Django templates, {{ user }} is a template variable provided by Django's authentication system when a user is logged in. It represents the currently logged-in user.

# When you use {{ user }} in your template, Django automatically substitutes it with the user object of the currently logged-in user. The user object contains various attributes
#  and methods related to the logged-in user, such as their username, email, and any other custom attributes you may have defined.

# So, in your dashboard template, when you include {{ user }}, it displays information about the currently logged-in user, such as their username or any other attribute you choose to display.
# In your case, it seems you're displaying the username of the logged-in user ({{ user.username }}) inside an <h4> tag.