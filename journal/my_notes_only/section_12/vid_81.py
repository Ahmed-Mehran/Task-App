

### RE STRUCTURING AND STYLING OUR DASHBOARD PAGE, WE WILL ALSO EXTEND THE NAVBAR, BY TEMPLATE INHERITANCE

## DASHBOARD PAGE IS GOING TO BE ONE OF THE MOST IMPORTANT PAGES, AS THIS IS THE PAGE THE USER IS GOING TO SEE AFTER LOGGING IN
## AND AFTER LOGGIN IN THEY SHOULD HAVE A GOOD SENSE OR VISIBILITY OF NAVIGATION ON THIS DASHBOARD PAGE. SEE AS THIS DASHBOARD
## WILL HAVE FUNCTIONALITY LIKE CREATING A THOUGH, DELETE A THOUGHT, SO WE WANT A NAVBAR FOR THOSE LINKS. WE ALSO WANT USERS TO BE 
## ABLE TO GO AHEAD AND MANAGE THEIR PROFILE, SO THAT IS SOMETHING WE WILL ADD IN AS WELL

### NOW WE WILL FIRST CREATE A NAVBAR THAT IS GOING TO BE INHERITED BY THIS DASHBOARD PAGE(LIKE WE HAD BASE.HTML IN CRM) AND BY ALL OF THE 
### FUTURE AUTHENTICATED PAGES, MEANING ONLY FOR THOSE PAGES, WHERE USER HAS LOGGED IN. WE WILL CREATE A NEW HTML TEMPLATE NAMED navbar.html

################ navbar.html



# {% load static %}

#  <html>

#     <head>

#         # these 3 lines aded from index.html and 4th from my-login.html
#         <meta charset="utf-8" />

#         <meta name="viewport" content="width-device-width, initial-scale=1, maximum-scale=1"/>

#         <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/morph/bootstrap.min.css">

#         <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">


#     </head>

#     ## HERE WE WILL WILL ADD THE NAVBAR COPIED FROM INDEX.HTML, WE WILL NOT CAHNGE THE LINKS BELOW FOR NOW, WE WILL DO IT LATER IN THE COURSE,RIGHT NOW ITS JUST
#     ## FOR EXTEDNING THE NAVBAR HERE , THAT WE DID BELOW. WE WILL JUST CHANGE THE LINKS FOR SOME LIKE DASHBOARD(AS WE KNOW THE URL FOR THAT)

#     ## NOW TO dashboard.html to extend this template and make other changes
    

#     <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-center">

#             <a class="navbar-brand main-heading"> 
                    
#               &nbsp; Edenthought
            
#             </a>
        
        
#             <button
#               class="navbar-toggler"
#               type="button"
#               data-toggle="collapse"
#               data-target="#navbarNavDropdown"
#               aria-controls="navbarNavDropdown"
#               aria-expanded="false"
#               aria-label="Toggle navigation"
#             >
#               <span class="navbar-toggler-icon"></span>
        
#             </button>
        
        
#               <div class="collapse navbar-collapse text-center" id="navbarNavDropdown">
        
                
#                 <ul class="navbar-nav ml-auto">  ## THESE POSITION THE NAVBAR LINKS OR ELEMNTS TO LEFT OR RIGHT ms for right and ml for left
        
        
#                   &nbsp;     &nbsp;     &nbsp; 
        
        
#                   <li class="nav-link">
              
#                     <a class=" nav-link "  href="{% url 'dashboard' %}">Dashboard</a>
        
#                   </li>
        
        
#                   &nbsp;     &nbsp;     &nbsp; 
                  
        
#                   <li class="nav-link">
        
#                     <a class="nav-link"  href=""> Create thought </a>
        
#                   </li>
        
        
#                   &nbsp;     &nbsp;     &nbsp; 

#                   <li class="nav-link">
        
#                     <a class="nav-link"  href=""> View thoughts </a>
        
#                   </li>
        
        
#                   &nbsp;     &nbsp;     &nbsp; 
                  
        
#                 </ul>
              
                
#               </div>
        
        
#         </nav>



#     ## this is for extending this navbar.html template, remember everything inside the below is unique to template and everyuthing outside the
#     ## block can be extended to other templates as well

#     {% block content %}


#     {% endblock %}



#  </html>





########################  dashboard.html

# {% extends 'journal/navbar.html' %}  ## HERE WE CAN SEE THAT WE ARE EXTENDING THE ABOVE TEMPLATE , remember with this extension the navbar 
# ##                                      properties will also extend like bootstrap properties to below html and to the html where its extended



# ## AND WE HAVE TO WRITE THE BELOW CONTENT NOW WITHIN THE BLOCK CONTENT (WE KNOW WHY) AND ALSO WE WILL AD SOME STYLING TO IT

# {% block content %}


## WE WAMT THIS DASHBOARD HEADING INSIDE A CONTAINER CLASS AND ADD SOME STYLE, SO WE WILL CONTAINER CLASS FROM MY-LOGIN.HTML(RIGHT AFTER HEAD TAG ENDS)
#     <div class="container bg-white shadow-md p-5 form-layout">
#         <h1> Dashboard</h1>


#         <a class="btn btn-outline-primary navbar-btn" type="button"  href="{% url 'user-logout' %}">logout Here</a>

#     </div>

# {% endblock %}          


######  THUS FROM ABOVE, WE HAVE CREATED A NAVBAR (NAVBAR.HTML) AND EXTENDED IN ONTO DASHBOARD.HTML
    




