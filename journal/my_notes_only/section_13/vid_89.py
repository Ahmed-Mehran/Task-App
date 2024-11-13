
## DELETE A THOUGHT-- [DELETE]

## NOW WE WILL ADD IN THE FUNCTIONALITY TO DELETE THE THOUGHT, AS WE WANT TO DLETE THE THOUGHT BY PARTICULAR ID, WE WILL AGAIN
## CHOOSE A DYNAMIC URL, SO THAT A PLACEHOLDER VALUE AN BE PLACE AND THEN PASSED IN HTML TEMNPLATE AS USER ID. ITS SIMILAR TO
## WHAT WE DID IN UPDATE, JUST THE VIEW FUNCTION DIFFERS

## FIRST OF ALL WE WILL CREATE A VIEW FUNCTION FO THIS

##########  VIEWS.PY

#### its totally similar to DELETE operation in the CRM project, just as we add the line user = request.user in Update lecture, we add that here as well

@login_required(login_url='my-login') 
def delete_thought(request, pk):

    thought = Thought.objects.get(id=pk, user=request.user)

    if request.method =='POST':

        thought.delete()

        return redirect('my-thoughts')



    return render(request, 'journal/delete-thought.html')


#####  NOW WE WILL EDIT THE HTML TEMPLATE FOR THIS

########################### DELETE-THOUGHT.HTML

## SEE WE BELOW HAVE A FORM , BUT ITS NOT FOR FILLING DATA, JUST AS SUBMIT OR PRESS DELETE BUTTON A FORM IS SUBMIITED WHICH CONTAINS THE
## DATA TO BE DELETED AND THUS WE HAVE FORM FOR THAT HERE(ALSO BEACUSE IN VIEW FUNCTION WE HAVE A POST REQUEST), 
# ALSO JUST ABOVE </div> TAG, YOU WILL SEE A HREF LINK, INCASE , YOU CHANGE YOUR MIND AND DONT WANT TO DELETE THE THOUGHT, THIS LINK
# WILL TAKE YOU BACK TO VIEW THOUGHTS


# {% extends 'journal/navbar.html' %}  

# {% block content %}

#     <br>

#     <div class="container bg-white shadow-md p-5 form-layout">
#         <h3> DDelete a thought</h3>

#         <br>
#         <br>
#         <form method = "POST" autocomplete="off" >

#             {% csrf_token %}

#             <br>

#             <button class="btn btn-secondary btn-md w-100 btn-block p-3" type="submit">  &nbsp; Delete Thought </button>

#         </form>

#        <a href="{% url 'my-thoughts' %}"> Return to thoughts </a>

#     </div>

#    


#     <br>
# {% endblock %}   



#### NOW THE LAST THING AS WE DID IN THE my-thoughts.html FOR HAVING THE UPDATE LINK(TO UPDATE THOUGHTS) WITH ITS CORROSPONDING ID(PK), WE WILL
#### DO THE SAME HERE, IN THE my-thoughts,html WE WILL ASLO HAVE A SAME LINK BUT WITH URL POINTING TO  'delete-thought' , SO JUST COPY PAST THE
#### UPDATE LINK AND JUST EDIT THE URL AND YOUR AE GOOD TO GO. BELOW IS WHAT LINK WILL LOOK LIKE

# <a button type="button" class="btn btn-outline-primary btn-sm"  href="{% url 'delete-thought' thoughts.id %}">Delete Thought</a>