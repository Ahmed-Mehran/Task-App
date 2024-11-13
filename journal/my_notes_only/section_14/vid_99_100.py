
##############     RESET OUR PASSWORD-- PART 1

### IN THIS LECTURE WE WILL BE INTERGRATING PASSWORD MANAGEMENT FUNCTIONALITY THAT WILL ALLOW OUR USERS TO RESET THEIR PASSWORDS
### WE WILL BE UTILIZING DJANGO'S BUILT IN VIEWS TO HANDLE OUR PASSWORD RESET URLS. 

## WE ARE ACTUALLY GOING TO SET EEVRYTHING UP IN THE URLS.PY, THAT IS THE MOST PART OF THIS LECTURE, SO WE DONT DEAL WITH ACTUAL VIEWS, WE ARE GOING TO USE DJANGO'S BUILT IN VIEWS
## NOW IN ORDER TO UTILIZE DJANGO'S BUILT IN VIEWS, WE NEED TO IMPORT IT IN THE URLS FILE ONLY

#################   URLS.PY


from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

# The line from django.contrib.auth import views as auth_views imports the views provided by Django's built-in authentication system (django.contrib.auth).

# Django provides a set of pre-built views and functionality for common authentication-related tasks, such as logging in, logging out, resetting passwords,
#  and managing user accounts. These views are part of the django.contrib.auth package.

# By importing these views as auth_views, you can easily use them in your Django project without having to write custom views for authentication tasks. For example, you can use 
# auth_views.LoginView to display a login form, auth_views.LogoutView to handle user logout, auth_views.PasswordResetView to initiate a password reset process, and so on.

# Importing these views as auth_views makes it clear that they are part of Django's authentication system, and it provides a convenient way to reference them in your code. It's a 
# common practice to use these built-in views for handling authentication tasks in Django projects, as they provide secure and reliable functionality out of the box.

## ACTUALLY WE ARE IMPORTING VIEWS,  using as auth_views is a stylistic choice that helps improve code readability and maintainability, making it easier for developers to 
## understand and work with authentication-related views in Django projects.


## NOW WE WILL ADD SOME URLS AT THE BOTTOM





urlpatterns = [
    
    path('',views.homepage,name=''),

    path('register',views.register,name='register'),

    path('my-login',views.my_login,name='my-login'),

    path('dashboard',views.dashboard,name='dashboard'),

    path('user-logout',views.user_logout,name='user-logout'),

    path('create-thought',views.create_thought,name='create-thought'),

    path('my-thoughts',views.my_thoughts,name='my-thoughts'),

    path('update-thought/<str:pk>',views.update_thought,name='update-thought'),

    path('delete-thought/<str:pk>',views.delete_thought,name='delete-thought'),

    path('profile-management',views.profile_management,name='profile-management'),

    path('delete-account',views.delete_account,name='delete-account'),


    ## ADD URL FROM HERE

    ## PASSWORD MANAGEMENT--WE ARE GOING TO CREATE FOUR URLS AND WE WILL DISCUSS EACH URL STEP BY STEP

    #### 1-- THE BELOW URL WILL ALLOW US TO ENTER OUR EMAIL IN ORDER TO RECEIVE A PASSWORD RESET LINK

    path('reset_password',auth_views.PasswordResetView.as_view(), name='reset_password'),

#   detail of  auth_views.PasswordResetView.as_view()  (the other a re simple routes and name convention that usually do)

# auth_views: This refers to a module in Django called auth_views. Django provides this module with pre-built views for handling authentication-related tasks like logging in, logging out, and resetting passwords.
# PasswordResetView: Within the auth_views module, there's a class-based view named PasswordResetView. This view is specifically designed by Django to handle the password reset functionality. It includes all the 
# necessary logic to display the password reset form, process the user's input, and send the password reset email.
# .as_view(): In Django, class-based views need to be converted into callable views that can be used by Django's URL dispatcher. The .as_view() method is a special method provided by Django that does this conversion
# . It takes the class-based view (PasswordResetView in this case) and turns it into a callable view function that Django can use to handle HTTP requests.
# So, when we use auth_views.PasswordResetView.as_view() in our URL configuration, we're essentially telling Django to use the PasswordResetView class-based view to handle requests to the specified URL pattern. Django
#  internally converts this class-based view into a callable view function that can process requests and generate responses for the password reset functionality. This allows us to use Django's built-in views seamlessly in our URL configuration.

    #### 2-- THI BELOW URL IS NOW GOING TO BE CONCERNED WITH SHOWING US A SUCCESS MESSAGE, SO WE CAN SAY SHOW A SUCCESS MESSAGE STATING THAT EMAIL WAS SENT

    path('reset_password_sent', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_done'),

# details of auth_views.PasswordChangeDoneView.as_view():

#  Here, auth_views refers to a module in Django that provides pre-built views for authentication tasks. PasswordChangeDoneView is a specific view provided
# by Django to handle the page shown after a successful password change. The .as_view() method converts this class-based view into a callable view function that Django can use in URL patterns.

    #### 3-- SEND A LINK TO OUR EMAIL SO THAT WE CAN RESET OUR PASSWORD, I.E THIS URL WILL BE USED TO SEND A PASSWORD RESET LINK

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

# details of above

# <uidb64>: This is a placeholder for a unique identifier encoded in base64. It's part of the URL and will be extracted by Django. It's used for identifying the user whose password is being reset.
# <token>: Similar to <uidb64>, this is another placeholder in the URL for a token. This token is also part of the URL and is used for security purposes to verify the authenticity of the password reset request.
# auth_views.PasswordResetConfirmView itself doesn't provide a link to reset the password directly. Instead, it's a class-based view provided by Django's authentication system to handle the confirmation of a password reset request.

# When a user requests a password reset and receives an email with a link containing a unique URL with a UID (user ID) and a token, clicking on that link will typically lead to a page where the user can enter a new password. This page
# is what auth_views.PasswordResetConfirmView handles. It provides the logic for verifying the user's identity based on the UID and token provided in the URL, and it presents a form for the user to enter and confirm their new password.

# So, while auth_views.PasswordResetConfirmView doesn't directly provide a link to reset the password, it's the view responsible for processing the password reset confirmation and presenting the user
# interface for setting a new password after clicking on the reset link.

    #### 4-- SHOW A SUCCESS MESSAGE THAT OUR PASSWORD WAS CHANGED

    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

# details of above auth_views.PasswordResetCompleteView.as_view()

# auth_views.PasswordResetCompleteView.as_view() is another class-based view provided by Django's authentication system. It is used to display a "password reset complete"
#  page to the user after they have successfully reset their password.

# After a user has completed the password reset process (i.e., they have entered a new password and submitted the form), Django will typically redirect them to a page indicating
#  that the password reset was successful. This is where auth_views.PasswordResetCompleteView comes into play.

# By using as_view(), you're converting the class-based view into a view function that can be used in Django's URL configuration.

# Here's how it works:

# The user successfully resets their password.
# Django redirects the user to the URL associated with auth_views.PasswordResetCompleteView.
# The view renders a template (usually provided by Django's authentication system) that informs the user that their password has been successfully reset.
# So, in summary, auth_views.PasswordResetCompleteView is used to display a confirmation message to the user after they've successfully completed the password reset process.


 
###  SEE THE ABOVE PARAMETERES ARE DEFAULT VALUES PROVIDED EVEN THE URL AND ALSO THE ROUTE NAME. SO WE CANT CHANGE THE ANY OF THE VALUES IN ABOVE PARAMATERS DEFINED  
###  THE ONLY THING THAT CAN BE OVERRIDDEN ABOVE IS THE BRACKETS WITHIN .as_view( in this bracket ), WE CAN OVERIDE THESE VIEWS WITH HTML TEMPLATES, WE WILL SEE 
###  THAT IN NEXT PART


]




##############     RESET OUR PASSWORD-- PART 2


####   NOW FIRST OF ALL WE ARE GOING TO CREATE FOUR TEMPLATES FOR THE FOUR URLS THAT WE CREATED, THEN WE WILL OVERRIDE THE URL WITH THOSE TEMPLATES




###############     password-reset.html  (TEMPLATE FOR 1ST URL CREATED)


## here we will create a simple form and some heading to describe the functionality to reset password



# <html>

       
#         <h3> Password reset </h3>

#         <br> 

#         <p> Forgotten your password? </p>

#         <br> 

#         <form method="POST" autocomplete="off">

#             {% csrf_token %}


#             {{form}}   ###  So this form in html template will generate form fields according to view in url i.e  auth_views.PasswordResetView.as_view()
#                        ###  so when you will pass this template in the url, it will generate fields acording to that



#             <br>

#             <input  type="Submit" name="Send email" >

#         </form>



# </html>



#####################  password-reset-sent.html   (TEMPLATE FOR 2ND URL CREATED)


## HERE WE WILL JUST DISPLAY THE MESSAGE AFTER THE EMAIL IS SENT.

# <html>


#         <h3> Password reset sent </h3>
        
#         <br>

#         <p> We've emailed you instructions for setting

#             a new password!

#         </p>

#     </div>


# </html>



#################       password-reset-form.html  (TEMPLATE FOR 3RD URL CREATED)

## THIS ONE IS GOING TO BE THE FORM THAT WE SEE WHEN WE ENTER IN OUR NEW PASSWORD

# <html>

       
#         <h3> Enter your new password</h3>

#         <br> 

#         <p> Please Enter your new password 
#             twice so that we can verify that your
#             typed it in correctly
#         </p>

#         <br> 

#         <form method="POST" autocomplete="off">

#             {% csrf_token %}

#             {{form}}    ## same as in password-reset, it will show the fiedls acording to its view in url

#             <br>

#             <input  type="Submit" name="Update Password" >

#         </form>



# </html>



#################       password-reset-complete.html  (TEMPLATE FOR 4th URL CREATED)


## THE AFTER FILLING OUT THE ABOVE FORM, PROCEED TO DISPLAY THE MESSAGE THAT PASWORD RESET HAS BEEN COMPLETED  

# <html>



#         <h3> Password reset complete </h3>

#         <br>

#         <p> Your password has been set.

#             <br> <br> You may go ahead and login to your account.

#         </p>

      #   <br>

      #   <a  href="/">Login</a>  ## we will set this up later

        


# </html>


#### NOW WE CREATED THE ABOVE TEMPLATES, WE WILL JUST OVERRIDE THE URL VIEWS WITH THESE TEMPLATES


###################   URL.PY



  ## NOW WE WILL OVERRIDE THESE BELOW URL VIEWS WITH THE TEMPLATES CREATED, WE WILL INSERT THE TEMPLATES IN BRACKETS IN .as_view( here )

    # path('reset_password',auth_views.PasswordResetView.as_view(template_name='journal/password-reset.html'), name='reset_password'),  # here we have inserted the html template related to 
    #                                                                                                                                   # url view, we will do the same for below i.e insert
    #                                                                                                                                   # their respective html template


    # path('reset_password_sent', auth_views.PasswordChangeDoneView.as_view(template_name='journal/password-reset-sent.html'), name=''password_reset_done''),

    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='journal/password-reset-form.html'), name='password_reset_confirm'),

    # path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='journal/password-reset-complete.html'), name='password_reset_complete'),



### NOW THE PASSWORD RESET FEATURE IS ADDED  

#####    REMEMBER WHENEVER YOU CREATE A NEW USER AND ASSOCIATE A EMAIL ADDRESS WITH THAT USER, AND IF YOU THEN PROCEED TO RESET PASSWORD, SO WHEN YOU ARE 
#####    FIRST PAGE OF PASSWORD RESET, IT WILL ASK FOR A MAIL, AND THE MAIL THAT YOU WILL BE PROVIDE, IF ITS LINKED WITH ANY OF THE USER IN THE DATABASE
#####    THE PASSWORD FOR THAT USER WILL BE RESET, REMEMBER WE NEED TO TYPE IN THE MAIL OF THE USER WHOSE PASSWORD WE WANT TO RESET AND NOT THE USER NAME
 


### the next viddeo is just testing our reset password functionality
