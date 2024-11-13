

##  LOGOUT OF AN ACCOUNT

## NOW AS WE LOGIN, WE NEED FUNCTIONALITY TO LOGOUT AS WELL

## BUT WE WILL HAVE TO CREATE A NEW LOGOUT VIEW FUNCTION FOR THIS, BUT ASLO REMEMBER TO PASS IN THE URL FOR THAT IN URLS.PY FILE

################## VIEWS.PY FILE  (LOGOUT VIEW)

#logout
def user_logout(request):

    auth.logout(request)

    return redirect('')




######### urls.py


    path('user-logout',views.user_logout,name='user-logout')



### NOW AS WE KNOW THAT WE WANT THE URL LINK OF THIS LOGOUT IN DASHBOARD, AS ITS WHERE WE ARE REDIRECTED TO AFTER LOGIN, THINK OF 
### THIS DASHBOARD AS ACCOUNT, WHERE WE LOGGED IN AND THEN IF WE WANT TO LOGOUT, WE WANT TO HAVE LOGOUT LINK ON THIS ACCOUNT PAGE


############## dashboard.py

# <h1> Dashboard</h1>


## add the below line

# <a class="btn btn-primary navbar-btn" type="button"  href="{% url 'user-logout' %}">logout Here</a>
        
 

