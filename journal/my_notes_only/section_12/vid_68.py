

#####  CREATING URLS AND VIEWS FOR THE NEW JOURNAL APP


## SEE AS THIS IS A NEW PROJECT, WE HAVE CONFIGURED EVERYTHING FROM START, FROM CREATING A NEW DJANGO DIRECTORY, THEN NEW VIRTUAL ENVS,
## THEN A NEW DJANGO APP I.E JOURNAL. AS WE ARE STARTING A NEW PROJECT, WE DID THIS. WE ALSO WILL CREATE EVERY FILE FROM SCRATCH.WE LINKED
## THE MAIN URLS TO THIS JOURNALS URLS.PY AS WELL. IF YOU WANT TO REWATCH THE CONFIGURATION OF THIS NEW PROJECT PLEASE WATC VIDEO 65,66,67 ON UDEMY
## BELOW ARE NEW VIEWS FUNCTION CREATED IN VIEWS.PY FILE AND ALSO THEIR URLS

############  VIEWS.PY FILE

from django.shortcuts import render

# Create your views here.
def homepage(request):

    pass

def register(request):
    
    pass


def my_login(request):

    pass


def dashboard(request):

    pass


################  URLS.PY

from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.homepage,name=''),

    path('register',views.register,name='register'),

    path('my-login',views.my_login,name='my-login'),

    path('dashboard',views.dashboard,name='dashboard')


]

