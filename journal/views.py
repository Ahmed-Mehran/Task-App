from django.shortcuts import render,redirect, HttpResponse

from .forms import CreateUserForm, LoginForm, ThoughtForm, UpdateUserForm, UpdateProfileForm  


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required  

from django.core.cache import cache

from django.contrib import messages


from .models import Thought, User, Profile

from django.core.mail import send_mail
from django.conf import settings


def homepage(request):

    return render(request, 'journal/index.html')


# register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False) 

            form.save() 

            send_mail("Welcome to Edenthought!","Congratulation on creating your acount", settings.DEFAULT_FROM_EMAIL, [current_user.email])  

            profile = Profile.objects.create(user=current_user) 
       
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

    current_user = request.user.id

    picture = Profile.objects.get(user=current_user)

    context = {'ProfilePic':picture}

    return render(request, 'journal/dashboard.html', context)




# CREATE
@login_required(login_url='my-login') 
def create_thought(request):

    form = ThoughtForm()
    
  #  cache_key = 'all_{}_thoughts'.format(request.user.id)

    if request.method == 'POST':

        form = ThoughtForm(request.POST)

        if form.is_valid():  

            thought = form.save(commit=False) 

            thought.user = request.user      

            thought.save()   
            
          #  cache.delete(cache_key) 

            return redirect('my-thoughts')

    context = {'CreateThoughtForm':form}        

    return render(request, 'journal/create-thought.html',context)

    
# READ    ####################        ###################################################################
@login_required(login_url='my-login') 
def my_thoughts(request):
    
    # cache_key = 'all_{}_thoughts'.format(request.user.id)

    # thought = cache.get(cache_key)
    
  #  if not thought:
       # return HttpResponse('Cache not working')

    thought = Thought.objects.all().filter(user=request.user)  
   # cache.set(cache_key, thought, 60*2)

    context = {'AllThoughts': thought}

    return render(request, 'journal/my-thoughts.html', context)



# UPDATE
@login_required(login_url='my-login') 
def update_thought(request, pk): 

    
   # cache_key = 'all_{}_thoughts'.format(request.user.id)

    thought = Thought.objects.get(id=pk, user=request.user.id)

    form = ThoughtForm(instance=thought)

    if request.method == 'POST':

        form = ThoughtForm(request.POST, instance=thought)
        
        if form.is_valid:

            form.save()
            
           # cache.delete(cache_key)

            return redirect('my-thoughts')

    context = {'UpdateThought':form}
    
    return render(request, 'journal/update-thought.html', context)




@login_required(login_url='my-login') 
def delete_thought(request, pk):
    
   # cache_key = 'all_{}_thoughts'.format(request.user.id)

    thought = Thought.objects.get(id=pk, user=request.user)


    if request.method =='POST':

        thought.delete()
        
       # cache.delete(cache_key)

        return redirect('my-thoughts')


    return render(request, 'journal/delete-thought.html')



# UPDATE USER
@login_required(login_url='my-login') 
def profile_management(request):

    current_user = request.user.id

    user = User.objects.get(id=current_user)

    form  = UpdateUserForm(instance=user)

   

    profile = Profile.objects.get(user=user) 

    form_2 = UpdateProfileForm(instance=profile)

 
    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=user)

        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)  



        if form.is_valid():

            form.save()

            return redirect('dashboard')
        
      

        if form_2.is_valid():

            form_2.save()

            return redirect('dashboard')

  

    context = {'ProfileForm':form, 'ProfileUpdateForm':form_2}

    return render(request, 'journal/profile-management.html', context)


@login_required(login_url='my-login') 
def delete_account(request):

    current_user = request.user.id

    user = User.objects.get(id=current_user)

    if request.method == 'POST':

        user.delete()
        
        return redirect('dashboard')

    return render(request, 'journal/delete-account.html')








