

###  CREATE AND REGISTER OUR THOUGHT MODEL

# IF YOU DONT UNDERTAND AT ANY POINT, JUST OPNE THE CRM PROJECT AND THERE WE HAVE EVERYTHING IN DETAIL

### SO FIRST OF ALL WE WILL BE CREATING A MODEL TO BE ABLE TO CREATE A OBJECT/THOUGHT AND STORE IT IN THAT MODEL/DATABASE

### SO OVER TO MODELS.PY



#################  MOELS.PY

from django.db import models

from django.contrib.auth.models import User

class Thought(models.Model):

    title = models.CharField(max_length = 150)
    content = models.CharField(max_length= 400)

    date_posted = models.DateTimeField(auto_now_add=True)  ## automatic puts in data and time when we create a object/task

    user = models.ForeignKey(User, max_lenth=10, on_delete=models.CASCADE , null=True)   ## CREATING A RELATIONSHIP WITH USER MODEL(THAT IS IMPORTED)
                                                                                         ## WE SET CASCADE IS EQUAL TO ON, BECAUSE IF THE USER IS BEING DELETD
                                                                                         ## AND IF THERE WA A THOUGH TASK REFERENCED TO IT, WHAT IS THE USE OF THAT TASK
                                                                                         ## AFTER THE REFERENCED USER HAS BEEN DELETED


## HOW THE ABOVE RELATIONSHIP WORKS AND WHAT WE CAN DO WITH THAT
# so this user field/relationship field generally has the access to all users(whatever user we create in User model) primary key in the User Model and then when we for example 
# select or get a primary key id from User model using database queries,  then as author field has access to all the id's of User, we just match that queried id from User model
# to author field and which ever id matches, we can that read, update or delete according to that



###  WHAT AND WHY WE ARE DOING


#  Importing the User model from django.contrib.auth.models and linking the Thought model to it allows us to associate each Thought object with a specific user.
# Let me explain it in simpler terms with an example:

# Imagine you have a blogging website where users can share their thoughts. Each user can create multiple thoughts (or blog posts). Now, you want to keep track
# of who wrote each thought so that you can display the author's name next to each post.

# Here's how the User model and the ForeignKey relationship help:

# Importing the User Model: We import the User model because it's already built into Django and provides a convenient way to manage user accounts
# , including authentication and authorization. We remember from CRM project that User was a default model/databse provided by Django with predefined
# fields and it included all the authentication capabilities and then to convert this to form we use UserCreationForm also provided by django, so we can
# created a form for User model

# Linking the Thought Model to the User Model: We use a ForeignKey field in the Thought model to create a relationship between thoughts and users. This means that each Thought
# object will be associated with a specific user. see many thoughts can belong to same user. but a thought cannot belong to more than 1 user.

# Benefits of Linking Thoughts to Users: By linking thoughts to users, we can do various things:
# Display the author's name next to each thought on the website.
# Allow users to view all thoughts written by a specific author.
# Implement features like filtering or searching for thoughts by author.
# Enforce access control, such as allowing only the author to edit or delete their own thoughts.

# In summary, importing the User model and linking the Thought model to it allows us to track which user created each thought, enabling various features related to user interaction
# and content management on our website.


# In simple words,  whe i Login as a user after registering, for example I have registered as Mehran, and now logged, now when I click on create a thought, that in future would be the view function for 
# creating thought and when I would have created a thought, it would be referenced to my user id that is mehran's user id through foreign key. w

# In summary, yes, your thought will be referenced to your user ID (Mehran's user ID) through a ForeignKey relationship, allowing Django to know that you are the author of that thought. 
# This ensures that each thought you create is tied to your user account and can be associated with you when displayed or managed in the application.


### NOW AS WE HAVE CREATED A A NEW MODEL AND WE REMEMBER WE HAVE TO MIGRATE IT TO OUR DJANGO DATABASE. FIRST RUN  python manage.py makemigrations TO PREPARE THE MIOGRATIONS 
### AND THEN TO PUSH THE MIGRATIONS TO SQL DATABASE, WE DO python manage.py migrate  and NOW OUR MODEL HAS BEN MIGRATED

## ALSO DONT FORGET TO REGISTER THE MODEL IN ADMIN.PY, SO WE CAN SEE AND VIEW THE MODEL IN ADMIN PANEL 



################### ADMIN.PY


from .models import Thought

admin.site.register(Thought)  ## NOW THE MOEDL IS REGISTER AND VIEWABLE ON DJANGO ADMIN PANEL


## ALSO CREATE A SUPER USER FOR THIS JOUNAL PROJECT(WE HAD CREATED ONE FOR CRM), SO TO CREATE A SUPER USER, DO python manage.py createsuperuser
## and enter your details and you would have now access to admin panel as super user 
