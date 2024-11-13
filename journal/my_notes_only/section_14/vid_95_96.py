
###  PROFILE MANAGEMENT-- UPLOAD A PROFILE PICTURE-- -----------------              PART 1

## IN THIS ELCTURE, WE WILL SET UP A FUNCTIONALITY THAT WILL ALLOW US TO GO AHEAD AND UPLOAD A PROFILE PICTURE TO OUR DJANGO APPLIATION

## SEE IF WE REMEMBER IN OUR LAST LECETURE, WE CREATE A PROFILE MODEL IN MODELS.PY AND GOT IT LINKED TO USER MODEL, NOW WE WILL CREATE A MODEL FORM FOR THAT IN FORMS.PY

##  NOW HEAD ONTO FORMS.PY

###################  FORMS.PY

## FORM FOR UPLOADING PROFILE IMAGE
class UpdateProfileForm(ModelForm):  ## or forms.ModelForm

    profile_pic = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:

        model = Profile
        fields = ['profile_pic']  ## will have the predefined customized profile_pic from above(line above class Meta)


## DETAILS OF THE LINE profile_pic = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control-file'})) AND WHY WE DEFINE IT BEFORE META CLASS

# forms.ImageField:  indicates that this field will handle image uploads.

# widget = forms.FileInput: This part specifies the type of input field that will be rendered in the HTML form. FileInput is a widget provided by Django that allows
# users to select files from their devices. So, this tells Django to render an input field of type file.

# attrs={'class':'form-control-file'}: Here, attrs stands for attributes, and it allows you to add extra attributes to the HTML element. In this case, you're adding a class attribute
# with the value 'form-control-file'.

# Class Attribute: The class attribute is used to apply CSS styles to HTML elements. By setting it to 'form-control-file', you're essentially assigning this class to the input field,
# which allows you to style it using CSS.
# so in short this line,  attrs={'class':'form-control-file'}, adds styling to profile image.Adding attrs={'class':'form-control-file'} to the ImageField widget ensures that the profile image field
# is styled using the predefined CSS rules associated with the 'form-control-file' class. This helps maintain a consistent and visually appealing appearance for file input fields, making the profile
# image input blend seamlessly with other form elements on the webpage.

# So, putting it all together, widget = forms.FileInput(attrs={'class':'form-control-file'}) is telling Django to render an input field for file uploads, and to apply the CSS class 'form-control-file' 
# to that input field. This helps you style the file input field according to your design requirements.

# We define the profile_pic field before the Meta class because it's specific to this form and not part of the model. We're customizing how the image field is displayed in the form by specifying the 
# widget and its attributes. The Meta class, on the other hand, provides information about the model associated with the form and which fields to include.
# By defining the profile_pic field before the Meta class, you're customizing its appearance and behavior specifically for this form(KIND OF SETTING THE DEFAULT FORM). SO EVEN IF WE PASS A EMPTY FORM
# IN VIEW FUNCTION, WE ALWAYS WILL HAVE THE profile_pic FIELD PREDEFINED ACCORDING TO ABOVE CUSTOMIATION DEFINED . 
# ALSO This allows you to control how the image upload field is rendered and displayed in the form, independent of how it's defined in the model
## Now When you include profile_pic in the fields list of your form's Meta class, it will render the field according to the specifications defined in the UpdateProfileForm class. So, it will display
## the field with the specified widget and any other customizations you've applied.


### NOW AFTER DEFINING THE ABOVE FORM, WE WILL HEAD ONTO VIEWS.PY FILE TO ACTUALLY WRITE SOME LOGIC TO RENDER THIS FORM

#################  VIEWS.PY FILE

# FIRST IMPORT THE ABOVE FORM TO VIEWS.PY

### SEE WE WONT BE CREATING ANY NEW VIEW FUNCTION FOR THIS. WE WILL BE EDITING THE REGISTER VIEW FUNCTION(def register(request):) BECAUSE WHEN WE  REGISTER USER, WE SHOULD HAVE A OPTION
### TO SET AND CHOOSE A PROFILE PICTURE. NOW IN TERMS OF THE FORM THAT WE CREATED AND IMPORTED (UpdateProfileForm), WE WILL GET TO THAT LATER ON WHEN WE HEAD ON OVER TO PROFILE MANAGEMENT
### FOR NOW WE WILL FIRST EDIT THE REGISTER VIEW FUNCTION


# register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False) ## we wont post the data straight away to database, current_user will contain all the details (field values) of the form, 
                                                   ## but those details are not yet saved to the database until you call form.save()

            form.save()  ## now the form is saved to database

    

            profile = Profile.objects.create(user=current_user) ## CREATES A NEW OBJECT/RCORD WHICH ALREADY HAS DEFAULT PIC VALUE AND THE ASSIGNS IT TO CURRENT_USER THAT IS BEING REGISTERED
                                                                ## WITH HELP OF user FIELD WHICH IS THE RELATIONSHIP FIELD AND WHICH LINKS THE Profile MODEL TO User MODEL.

            ## SO AS SOON AS THE USERS CREATED(current_user), THEN WITH THAT A PRFOILE OBJECT WITH DEFAULT VALUE WILL BE CREATED AND THEN THEY ARE LINKED TOGETEHER BY user FIELD
            ##(user FEILDIS RELATONSHIP FIELD OF Profile MODEL AND IS LINKED TO USER MODEL) AS user = curent_user  AND THUS CURRENT_USER IS NOW LINKED TO THIS PROFILE OBJECT BY user field

## DETAILS OF THIS LINE, profile = Profile.objects.create(user=current_user)
# When you use Profile.objects.create(), you are indeed creating a new instance (or object) of the Profile model and saving it to the database in a single step.

# user is a ForeignKey field in the Profile model, then by using Profile.objects.create(user=current_user), you are creating a new Profile object and associating it with the current_user provided.
# current_user contains the detail of newly created user. user=current_user assigns the current_user instance (which represents the user created from the form data) to the user field of the PROFILE MODEL
# This ensures that a new Profile instance/record is created and associated with the current_user correctly.
# So, when you call Profile.objects.create(user=current_user), Django does the following:

# It creates a new Profile object.
# It sets the user field of the newly created Profile object to the current_user object provided.
# It saves this new Profile object to the database, establishing the relationship between the Profile and the User.
# In summary, Profile.objects.create(user=current_user) is a concise way to create a new Profile object and associate it with a specific user (current_user) in one step, using Django's ORM.

####  why we create a profile object and how can a profile object be created without adding a profile picture as in model field its an Image field
## SEE WE CREATE A PROFILE OBJECT, BECAUSE AS SOON AS THE NEW USER IS REGISTERED, WE WANT TO BIND THAT USER TO THIS NEWLY CREATED PROFILE OBJECT. SO ITS COMMON SENSE, EVERY NEW USER
## WILL HAVE A SEPARATE PROFILE OBJECT/IMAGE AND WHEN A NEW USER WILL BE RESGITERED/CREATED, WE CREATE A NEW PROFILE OBJECT WITH DEFAUL PARAMETERS AND BY DFEFAULT PARAMETERS WE MEAN AS WE HAVE THIS LINE
## Profile.objects.create(user=current_user), SEE THIS LINE, WE COULD HAVE DEFINED LIKE THIS profile = Profile.objects.create(user=current_user, profile_pic='custom_profile_pic.png')
## SO YOU CAN NOTICE WE HAVE ONLY ONE FIELD IN Profile MODEL WHICH CAN TAKE INPUT AND THAT IS profile_pic and IN THIS LINE WE HAVE GIVEN A VALUE OR CREATED A OBJECT CALLED 'custom_profile_pic.png'
## TO THIS profile_pic field. BUT WE DONT DO THAT, WE KEEP IT BLANK, WE DONT ASSIGN ANY VALLUE TO. BUT YOU NOW THINK, HOW CAN ONE CREATE AN OBJECT AND DOESNT ENTER ANY RECORD OR VALUE
## BUT IF YOU SEE IN THE Profile MODEL and SPECIFICALLY THIS FIELD i,e profile_pic : This field is an ImageField which allows users to upload an image to their profile. It's optional
## (null=True and blank=True), meaning users can choose not to upload a profile picture. The default parameter specifies the default image filename if no image is uploaded. SEE WE HAVE AN OPTION TO
## LEAVE IT BLANK FOR NOW, BUT ALSO WE HAVE DEFAULT VALUE THAT IS ALREADY DEFINED(A DEFAULT IMAGE PER SAY).NOW IN CASE WE DDINT HAD A DEFAULT VALUE, WE STILL CAN LEAVE BLANK WHILE DOING Profile.objects.create 
## BECAUSE WE HAVE NULLABLE AND BLANK = TRUE.  WE DO THIS BECAUSE WE WANT A DEFAULT IMAGE FOR EVERY USER THAT IS REGISTERED AND DEFAULT IMAGE SHOULD BE SAME. THEN LATER ON WE WILL ADD SOME FUNCTIONALITY WHERE WE CAN CHANGE THE USER'S DEFAULT IMAGE. 
## Profile.objects.create(user=current_user), it will automatically use the default profile picture 'Default.png' for the profile_pic field unless you explicitly provide a different value.

       
            messages.success(request, "User created")

            return redirect('my-login')

    context = {'RegistrationForm': form}

    return render(request, 'journal/register.html', context)

# SO IN SHORT FOR ABOVE CODE,we're handling user registration. When a user submits the registration form, we first instantiate a CreateUserForm object to collect the user's input. If the form is submitted via POST request and is valid, we use form.save(commit=False) 
# to create a new user instance without immediately saving it to the database. This gives us the opportunity to perform any additional operations or modifications on the user object if needed. Then, we call form.save() to save the user
# data to the database. After that, we create a new Profile object using Profile.objects.create(user=current_user), associating it with the newly created user. This ensures that every user has a corresponding profile object. Finally,
#  we display a success message and redirect the user to the login page. Overall, this code captures the user's registration information, saves it to the database, creates a corresponding profile object, and handles the user's redirection.

###  SEE NOW WHAT HAPPENS, WHEN YOU WILL RUN THE SERVER I.E http://127.0.0.1:8000/. GO ONTO REGSITER AND REGISTER A NEW USER. NOW GO TO admin DASHBOARD OF DJANGO AND IF YOU CLICK ON 
###  Pofiles, YOU WILL SEE A PROFILE OBJECT WOULD BE CREATED AUTOMATICALLY AND THE user FIELD OF THE PROFILE OBJECT WOULD HAVE THE NAME OF NEW REGISTERED USER ASSOCIATED WITH IT.
### AND ALSO YOU WILL SEE A DEFAULT PIC ASSIGNED TO THE PROFILE OBJECT AND THIS HOW OUR NEWLY CREATED/REGISTERED USER WILL ASSIGNED TO NEWLY CREATED PROFILE OBJECT



####  NOW AS WE KNOW THAT WHEN USER IS REGISTERED/CREATED, A DEFAULT IMAGE IS ASSOCIATED WITH IT. WE ALSO KNOW WHEN WE CREATE USER, WE THEN LOGIN AND WE ARE REDIRECTED TO
####  DASHBOARD, WHAT WE WANT TO DO IS THAT, WE WANT TO RENDER THIS DEFAULT IMAGE ON THE DASHBOARD PAGE AS WELL, SO WHEN THE USER AGAIN LOGS IN  ONTO DASHBOARD, A DEFAULT PICTURE
####  IS AT DISPLAY ON THE DASHBOARD. SO FOR THIS WE WILL FRIST ADD SOME FUNCTIONALITY TO DASHBOARD VIEW FUNCTION

################# VIEWS.PY(DASHBOARD)


@login_required(login_url='my-login')
def dashboard(request):

    current_user = request.user.id

    picture = Profile.objects.get(user = current_user)

    context = {'ProfilePic':picture}

    return render(request, 'journal/dashboard.html', context)

### SEE WHAT WE HAVE DONE ABOVE IS THAT WE HAVE FIRST STORE THE LOGGED USER ID CURRENT_USER, THEN WITH HELP OF GET QUERY, I CHECCKED IN DATABSE IF THERE IS AN USER THAT MATCHES
### THE CURRENT_USER(ID) AND IF THERE IS, STORE IT IN picture variable AND THIS CONTEXT DICTIONARY WILL HELP US TO RENDER THIS IMAGE ON WEBPAGE. NO WE WILL MAKE THE CHANGES IN
### DASHBOARD.HTML AS WELL

######################  DASHBOARD.HTML


# {% extends 'journal/navbar.html' %}  



# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">

#         <h1> Dashboard</h1> <h4>{{user}}</h4>  

#         <br> <br>

#         ## HERE WE MAKE THE CHANGE, REMEMBER AS WE ARE RENDERING OUT AN OBJECT, WE NEED TO MENTION THE OBJECT FIELD/ATTRIBUTE AS WELL, AS WE HAVE ONLY ONE FIELD/ATTRIBUTE IN PROFILE MODEL
#         ## I.E THE profile_pic FIELD. SO THAT IS WHY WE DO ProfilePic.profile_pic AND AS WE HAVE TO RENDER OUT AN IMAGE, THAT IS WHY WE ALSO ATTACH .URL BELOW
#         <img src="{{ProfilePic.profile_pic.url}}"
  

#         <a class="btn btn-outline-primary navbar-btn" type="button"  href="{% url 'user-logout' %}">logout Here</a>

#     </div>

# {% endblock %}    


### NOW BELOW IS THE SAME ABOVE DASHBOARD HTML BUT WITH SOME STYLING AND ADJUSTMENT TO ADJUST THE IMAGE AND LOOK GOOD ON WEB PAGE


# {% extends 'journal/navbar.html' %}  



# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">

#         <h1> Dashboard</h1> 

#         <br> <br>

#         <img style="width:110px; height:90px;" src="{{ ProfilePic.profile_pic.url }}">
#         <br><br>
#         <h2>{{user}}</h2>  

#         <br>
#         <br>

#         <a class="btn btn-outline-primary navbar-btn" type="button"  href="{% url 'user-logout' %}">logout Here</a>

#     </div>

# {% endblock %}    



############------------------------------------------------               PART 2


### NOW WE WILL GO AND MANAGE OUR profile_management VIEW FUNCTION. AS WE HAD IMPORTED UpdateProfileForm, WE WILL ACTUALLY MAKE USE OF THAT FORM TO UPDATE THE PROFILE PICTURE. SEE IN OUR PROFILE MANAGEMENT, 
### WE NEED TO SET UP AN AREA WHERE WE CAN GO AHEAD AND UPLOAD OUR PROFILE PICTURE. NOW OVER TO PROFILE MANAGEMENT VIEW FUNCTION

######################  VIEWS.PY(profile_management)


# UPDATE USER
@login_required(login_url='my-login') 
def profile_management(request):

    current_user = request.user.id

    user = User.objects.get(id=current_user)

    form  = UpdateUserForm(instance=user)

    ## NOW WE WANT TO DOS I WE WILL DO A DATABASE QUERY AND WE WILL GETH PROFILE PICTURE ACCORDING TO THE USER LOGGED IN

    profile = Profile.objects.get(user=user)  ## HERE FIRST user IS THE DATABASE QUERY TO GET SOME USER FROM DATABSE AND SECOND user IS THE ABOVE user THAT WE GO BY QUERYING THE ID

    ## THE ABOVE LINE CAN BE SIMPLY WRITTEN AS,  profile = Profile.objects.get(user=request.user)  ## means get the Profile object of current user loggedd in
    # NOW WE WILL PUT THE DATA IN THE FORM THAT WE IMPORTED I.E UpdateProfileForm. REMEMBER THE profile_pic FIELD (THE ONLY FIELD AVAILABLE FOR THIS FORM) HAS THE CAPABILITY
    # TO UPLOAD FILES, WHICH IS DEFINED BY FIRST LINE ABOVE CLASS META IN FORMS.PY FOR UpdateProfileForm
    form_2 = UpdateProfileForm(instance=profile)

 
    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=user)

        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)  

## DETAILS OF ABOVE LINE

# request.FILES is a dictionary-like object that holds uploaded files submitted as part of a form. In Django, when you have a form that includes a file 
# input field (e.g., <input type="file">,WHICH WE HAVE), you need to use request.FILES to access the uploaded file data.

# When a form includes a file input field and is submitted, the file data is sent as part of the request body in a different format compared to regular
# form data. Django handles this uploaded file data separately from regular form data and stores it in the request.FILES object.

# request.POST contains the form data submitted via POST request, while request.FILES contains the uploaded file data. When handling a form that includes both regular form data and 
# file uploads, you need to include both request.POST and request.FILES when instantiating the form. This ensures that Django properly handles both types of data during form processing.

# SO form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile) is used to instantiate the UpdateProfileForm form with both regular form data (request.POST) and uploaded
# file data (request.FILES). This allows the form to handle both types of data during form processing, ensuring that the profile picture upload is properly handled.



#         if form.is_valid():

#             form.save()

#             return redirect('dashboard')
        
#         ## WE HAVE TO DO FORM CHECK FRO form_2 SEPARATELY, BECAUSE ITS GOING TO CONSIST OF PROFILE PICTURE ONLY

#         if form_2.is_valid():

#             form_2.save()

#             return redirect('dashboard')

#     ## NOW IN THE CONTEXT DIC WE ARE GOING TO PASS IN THE SECOND KEY AND VALUE FOR form_2

#     context = {'ProfileForm':form, 'ProfileUpdateForm':form_2}

#     return render(request, 'journal/profile-management.html', context)

# ### NOW WE HAVE TO RENDER OUT THIS NEW form_2 WITH HELP OF ITS KEY THAT IS 'ProfileUpdateForm' AND WE WILL EDIT THE profile-management.html FILE FOR THIS

# #####################  profile-management.html

# ### SEE WE HAVE TO NOW HAVE A FORM FIELD TO UPDATE PROFILE PICTURE, SO WE WILL JUST COPY THE WHOLE CONTAINER PART AND MAKE A COPY OF IT BELOW SO THAT IS DISPLAY UNDER THE UPDATE USER
# ### ON WBBPAGE, WE WILL ALSO A HAVE A FORM IN IT, AS WE ARE UPDATE THE FIELDS OF USER PROFILE FORM OR WE CAN SAY UPDATE THE USER PROFILE PICTURE

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

#             <br>
#             <br>



#             <a button type="button" class="btn btn-outline-danger btn-sm" href="{% url 'delete-account' %}">Delete account</a>


#         </form>

# ### FROM HERE WE HAVE EDITED FOR THE PROFILE PICTURE UPDATE PART

#     </div>

#      <div class="container bg-white shadow-md p-5 form-layout">

#         <h3> Update Profile Picture </h3>  ## change text here

#         <br>
#         <br>

#          #### HERE BELOW (VERY IMPORTANT), SEE HERE IN OUR FORM, IN ORDER TO ALLOW FILES TO BE PUSHED, IF YOU REMEMBER WE ARE UPLOADING FILES AND IN VIEWS FUNCTION WE ALSO HAVE 
#          #### request.FILES. IN ORDER FOR THIS PROPERTY TO WORK, WE WILL HAVE TO ADD AN ATTRIBUTE HERE IN BELOW FORM i.e enctype="multipart/form-data"

#         <form method = "POST" autocomplete="off"  enctype="multipart/form-data">

#             {% csrf_token %}

#             {{ ProfileUpdateForm |crispy }}  ### INSERT THE KEY FROM VIEWS FUNCTION TO RENDER THE FORM



#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Update Profile Picture </button>

#             <br>
#         </form>

#     </div>

#     <br>
# {% endblock %}   



### NOW AFTER UPDATING PROFILE PICTURE IF YOU WILL GO TO media FOLDER UNDER ROOT DIRECTORY, YOU WILL SEE THE PICTURE YOU UPDATED HAS BEEN SAVED THERE

