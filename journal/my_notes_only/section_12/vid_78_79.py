
## ADD STYLING TO OUR FORMS-- PART 1

## WE WILL IMPROVE THE LOOKS OF  HTML PAGES SUCH AS REGISTER AND MY-LOGIN PAGE



## FIRST OF ALL LETS EDIT THE REGISTER.HTML

# {% load static %}   ### to load our static file( the css file)

# <html>

#     <head>

#         <title> Edenthought | Register </title>
#         <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/morph/bootstrap.min.css">  

#         ## FIRST OF ALL WE COPIED THE ABOVE LINK FROM index.html FROM HEAD SECTIO, SO THAT THE BOOTSTRAP THEME COULD BE IMPORTED HERE AS WELL

#         ## NOW AS WE HAVE BOOTSTRAP LINK ATTACHED, WE CAN ADD SOME BOOTSTRAP FUNCTIONALITY

#         ## SEE AS SIZE OF OUR FORM IS WAY T BIG, SO WE WILL IMPORT IN CSS FILE FROM STATIC FOLDER UNDER JOUNAL ROOT DIRECTORY to re adjust the size
#         <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">  

#         ## NOW WE HAVE TO REFERENCE THSI CSS FILE THAT WE IMPORTED SO THAT THE CHANGE COULD BE SEEN ON THE WEBPAGE

#     </head>

#     <br>


#     ## REFERENCE THE CSS FILE HERE IN CLASS
#     <div class = "container bg-white shadow-md form-layout" >  ### we set the background of form in white colour  and also a shadow effect
                                                                 ## form-layout is the css functon that is referenced


#         <h2> Create your account </h2>

#         <h3> Share your thoughts today </h3>

#         <br>
#         <br>
      

#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ RegistrationForm.as_p }}


          
            
#             ## WE WILL ASLO STYLE IN THE CREATE ACOUNT BUTTON WITH THE HELP OF BOOTSTRAP i.e this part below class="btn btn-secondary btn-lg w-100 btn-block p-4"
#             ## we have added by help of bootstrap

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type = "submit"> &nbsp; Create Account </button>

#         </form>




#     </div>

#     <br>


# </html>


##  NOW WE WILL EDIT THE LOGIN FORM AS WELL i.e my-login.html

## SO LIKE WE COPIED THE DESIGN FOR REGISTER.HTML FROM INDEX.HTML, NOW WE WILL COPY THE SAME DESIGN FOR my-LOGIN.html  FROM REGISTER.HTML
## WE JUST IMPORT THE STYLING ETC ETC THAT WE HAD IMPORTED IN REGISTER.HTML

############### my-login.html

# {% load static %}

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

#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ LoginForm.as_p }}


#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Login </button>

#         </form>

#     </div>

#     <br>


# </html>



############################   VID_79

## SEE THIS ALSO IS A PART OF STYLING OUR MY-LOGIN AND REGISTER HTML, BUT HERE WE IMPROVE THE LOOK OF FORM FIELDS, THAT IS THE BLANK SPACE, WHERE
## USER ENTERS HIS DATA. SO WE WILL IMPROVE THE STYLING OF THESE FIELDS

## TO DO SO, WE JUST UTILIZE THE CRISPY BOOTSTRAP FIVE PACKAGE, WHICH IS GOING TO ALLOW US TO IMPROVE THE OVERALL LOOK FOR OUR FIELDS

## FIRST do, pip install crispy-bootstrap5, in your terminal within your environment

## SO AFTER RUNING THE ABVE LINE, WE WILL GO TO SETTINGS.PY AND IN INSTALLED APP, UNDER JOURNAL, WE WILL INSERT THESE TWO LINES
"crispy_forms",
"crispy_bootstrap5"

##  AND JUST UNDER THIS, BUT OUTSIDE OF PARAMETERS THAT IS OUTSIDE THE BRACKET, WRITE THIS LINE AS WELL

## CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
## CRISPY_TEMPLATE_PACK = "bootstrap5"

## the above is kind of filter and we can apply them to any of our template, like we wil apply to my-login and register.html

## ADD THIS LINE, {% load crispy_forms_tags %} , IN BOTH REGISTER AND MY-LOGIN.HTML UNDER THIS LINE {% load static %}
# ALSO UNDER THE LINE {% csrf_token %} IN FORMS, WE HAVE TO EDIT THE TEMPLATE INHERITANCE VARIABLE AND IT WILL BE LIKE BELOW

##  {{ LoginForm|crispy }}  --for login form
## {{RegistrationForm|crispy}} -- for registration form

## and thus our styling of form fields will be improved







