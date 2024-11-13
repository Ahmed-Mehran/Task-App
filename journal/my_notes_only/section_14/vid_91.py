
#####   PROFILE MANAGEMENT-- DELETE AN ACCOUNT

## NOW AS WE HAVE WRITTEN FUNCTIONALITY FOR REGISTERING USERS, LOGGING IN THE USER AND ALSO UPDATING THE USER. NOW WE WILL ADD IN FUNCTIONALITY
## TO DELETE USER

## NOW WILL FIRST OF ALL CREATE A NEW VIEW FUNCTION FRO THIS AND ALSO A CORROSPODNING TEMPLATE AND WILL ADD THE VIEW FUNCTION IN URL PATH AS WELL

## WE WONT BE CREATING ANY FORM FOR THE DELETE FUNCTION, AS WE DONT REALLY NEED A FORM TO DELETE SOMETHING, WE WILL JUST GO ONTO VIEWS.PY FILE
## AND EDIT THE DELETE FUNCTION


############  VIEWS.PY FILE (delete_account)


@login_required(login_url='my-login') 
def delete_account(request):

    current_user = request.user.id

    user = User.objects.get(id=current_user)

    if request.method == 'POST':

        user.delete()
        
        return redirect('dashboard')

    return render(request, 'journal/delete-account.html')

## THIS IS VERY SIMPLE AND ALMOST SAME THING AS DELETE THOUGHT, WE GET THE ID OF CURRENT USER AND BY THAT WE GET THE CURRENT USER LOGGED IN
## THEN ON POST REQUEST, USER IS DELETED


## NOW WE WILL EDIT THE DELETE-ACCOUNT.HTML

############     DELETE-ACCOUNT.HTML

###  WE HAVE JUST COPIED FROM DELETE-THOUGHT.HTML AND HAVE MADE THE NECESSARY CHANGES, SEE BELoW,  ABOVE </DIV> TAG, WE HAVE A HREF LINK
###  FOR EXAMPLE, IF THE USER IS ON DELETE PAGE AND DOESNWANT TO DELETE, SO WE HAVE PUT UP A LINK WHILE WILL RETURN HIM TO PROFILE MANAGEMENT 

# {% extends 'journal/navbar.html' %}  

# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">
#         <h3>Sure Want to delete your account</h3>

#         <br>
#         <br>
#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}


#             <button class="btn btn-outline-danger btn-md w-100 btn-block p-3" type="submit">  &nbsp; Delete Account </button>

#         </form>

#         <br>

#         <a href="{% url 'profile-management' %}"> Return to Edit Profile </a>

#     </div>

    

#     <br>
# {% endblock %}   


#### SEE AS IN LAST LECTURE, WE UPDATED THE USER, THAT WE KIND OF DID PROFILE MANAGEMENT, NOW WE WANT IN THAT UPDATE WEBPAGE IS THAT BESIDES HAVING THE
#### UPDATE FUNCTIONALITY, WE WILL ALSO SET UP A HREF LINK THAT WILL REDIRECT THE USER TO DELETE ACCOUNT. SO USER HAS THE OPTION TO GO AND DELETE ACCOUNT
#### FROM UPDATE OR profile-management PAGE. NOW ONTO PROFILE-MANAGEMENT.HTML

################# profile-management.HTML




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

#             ## ADD IN THE BELOW LINE, JUST COPIED THIS LINE FROM my-thoughts.html AND NOW YOU WILL HAVE A BUTTON WHICH WILL REDIRECT
#             ## YOU TO delete-account.html Page

#             <a button type="button" class="btn btn-outline-primary btn-sm" href="{% url 'delete-account' %}">Delete account</a>


#         </form>

#     </div>

#     <br>
# {% endblock %}   


