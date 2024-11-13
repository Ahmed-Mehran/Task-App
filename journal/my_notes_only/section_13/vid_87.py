
###### UPDATE A THOUGHT--[UPDATE]

### SO THIS IS THE UPDATE PART OF THE CRUD OPERATIONS, AS WE HAVE DONE THE CREATE PART AND READ OF CRUD, WE NEED SOME FUNCTIONALITY TO UPDATE AND IN THIS LECTURE
### WE WILL DO THAT.



######  FIRST OF ALL AS WE WANT TO UPDATE A THOUGHT, WE WILL CREATE A NEW VIEW FUNCTION FOR THIS AND ALSO ADD IN THE URL FOR THE NEW VIEW FUNCTION IN URLS.PY
###### REMEMBER TO MAKE THE URL DYNAMIC, BECAUSE ITS WHAT WE USED TO DO WITH UPDATE OPERATIONS

################# VIEWS.PY FILE

## SEE THIS BELOW UPDATE FUNCTION IS TOTALLY SIMILAR TO UPDATE FUNCTION IN THE CRM PROJECT AND ALSO THE PK (PLACHOLDER) FUNCTIONS THE SAME
## NOTHING IS DIFERENT, ONLY ONE LINE IS ADDED IN THE QUERY LINE I.E user=request.user

# UPDATE
@login_required(login_url='my-login') 
def update_thought(request, pk):

    
     # as we know pk is the palceholder, generally referencing to primary key

    ## now we will grab the thought object that we want to update by Pk(primary key) 

    thought = Thought.objects.get(id=pk, user=request.user)## When we write user=request.user in the query, it means we're filtering the Thought objects to only retrieve the thought
                                                            ## that belongs to the currently logged-in user.this part of the query ensures that we're only updating thoughts that belong to the user who 
                                                            ## is currently logged in, providing a layer of security and ensuring data integrity within the application.
                                                            ## WATCH VIDEO 88(TRY AND EXCEPT EROR HANDLING ON UDEMY) TO BEST UNDERSTAND WHY WE USE THIS LINE THAT IS user=request.user
                                                            ## if we dont include user=request.user, anybody can just come and update any thought



    form = ThoughtForm(instance=thought)

    if request.method == 'POST':

        form = ThoughtForm(request.POST, instance=thought)
        
        if form.is_valid:

            form.save()

            return redirect('my-thoughts')

    context = {'UpdateThought':form}
    
    return render(request, 'journal/update-thought.html', context)




##### NOW AS WE HAVE CREATED THE UPDATE FUNCTION, WE KNOW THAT WE HAVE A my_thoughts FUNCTION TO VIEW THOUGHTS, DISPLAYING ON NAVBAR AND CLICKING ON IT
##### TAKES US TO THE PAGE WHERE WE CAN VIEW THE THOUGHTS OF THE SPECFIC USER, BUT NOW AS WE WE HAVE CREATE A NEW FUNCTION I.E UPDATE FUNCTION.
##### WE SHOULD HAVE DIRECT HREF LINK OF THIS UPDATE TASK, RIGHT IN OUR VIEW THOUGHTS PAGE. SO WE CAN EASILY SEEE/VIEW  OUR THOUGHTS AND 
##### WE KNOW WHICH THOUGHT TO UPDATE. SO FIRST OF ALL IN THE my-thoughts.html add the link

##################  my-thoughts.html



# {% extends 'journal/navbar.html' %}  


# {% block content %}

    

#     <br>

#     {% for thoughts in AllThoughts %}
#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">


#             {{thoughts.title}}

#             <br>

#             {{thoughts.content}}

#             <br>

#             {{thoughts.date_posted}}

#             <br>
#             <hr>

#             {{thoughts.user}}




            
#             ###   HERE WE ADD IN THE URL AND ALSO THE PLACEHOLDER VALUE, THIS URL WITH PK NOW BELONGS TO THE PARTICULAR THOUGHT CREATED
#             ###   BY THAT USER ( THATS WHY WE REFERENCE ID)

#             <a href = "{% url 'update-thought' thoughts.id %}"> Update Thought </a>

              ##  BY ABOVE NOW, WHEN WE WILL CLICK ON THIS LINK, FIRST OF ALL update-thought WILL BE PLACE IN THE URL(SEARCH BAR) ABOVE WITH THE
              ## PLACE HOLDER VALUE(DYNAMIC URL), SUPPOSE THE id = 2, NOW THIS ID WILL BE PASSED ONTO UPDATE FUNCTION ALONG SIDE REQUEST IN THE
              ## pk (as pk was a placeholder) AND THEN THE GET QUERY WILL GET THE ID OF THOUGHT BY THIS PK VALUE (AS id=pk in get query) AND THEN WE WILL UPDATE THE
              ## FORM AS USUAL

#         <br>
 
#     </div>

#     {% endfor %}

#     <br>
# {% endblock %}   


###  NOW WE WILL EDIT THE update-thought.html FOR THIS LECTURE

#####################  update-thought.html

####   WE WILL COPY THE CONTENTS FROM create-thought.html as this involves a form submission and do the minor changes


# {% extends 'journal/navbar.html' %}  

# {% load crispy_forms_tags %}


# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">
#         <h3> Update Thought</h3>

#         <br>
#         <br>
#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             {{ UpdateThought|crispy }}



#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Update Thought </button>

#         </form>

#     </div>

#     <br>
# {% endblock %}   

