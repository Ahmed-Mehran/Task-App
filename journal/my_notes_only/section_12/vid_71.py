

###  RE STRUCTURING AND STYLING OUR HOMEPAGE

####  WE WILL JUST REPLACE THE INDEX.HTML FILE WITH INDEX.HTML FROM THE RESOURCE PROVIDED BY UDEEMY COURSE, AS IT HAS A LOT OF BOOTSTRAP CONTENT, SO ITS BEST TO COPY
####  AND JUST UNDERSTAND THE FILE

## PLEASE REVISE THE HTML, CSS AND BOOTSTRAP PART FROM FLASK COURSE THAT YOU HAD TAKEN. READ BOOTSWATCH AS WELL FOR THE THEMES OF WEB PAGES

## DETAIL OF FILE IS BELOW


# {% load static %}  ## WE KNOW THAT IN DJANGO, WE USE THIS TO LOAD STATIC FILES

# <!DOCTYPE html>

#     <html lang="en">

#         <head>

#           <title> Edenthought </title>


#           <meta charset="utf-8" />

#           <meta name="viewport" content="width-device-width, initial-scale=1, maximum-scale=1"/>


#           <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/morph/bootstrap.min.css">   ### HERE WE LINK THE BOOTSTRAP CSS FILE


#           <link rel="stylesheet" type="text/css" href=" ">   ### HERE ALSO WE LINK THE CSS FILE, BUT ITS EMPTY FOR NOW, AS WE WILL LOAD OUR CUSTOM FILES LATER



#  <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-center">  ##HERE YOU CAN NOTICE WE START WITH BUILDING OUR NAV BAR AND THIS NAVBAR IS BASED ON BOOTSTRAP NAVBAR

#             <a class="navbar-brand main-heading"> 
                    
#               &nbsp; Edenthought   
            
#             </a>
        
        
#             <button                  ### THESE ARE FOR RESPONSIVE BUTTONS IN NAV BAR, FOR EXAMPLE WE SHRINK OUR WEBSITE AND WE HAVE THREE BARS WHICH WE CAN CLICK ON AND IT WILL SHOW 
                                       ### ALL THE BUTTONS ON NAVBAR
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
        
                
#                 <ul class="navbar-nav ms-auto">
        
        
#                   &nbsp;     &nbsp;     &nbsp; 
        
        
#                   <li class="nav-item">
              
#                     <a class="btn btn-primary navbar-btn" type="button"  href="">Register</a>   ### REGISTER BUTTON ON NAVBAR
        
#                   </li>
        
        
#                   &nbsp;     &nbsp;     &nbsp; 
                  
        
#                   <li class="nav-item">
        
#                     <a class="btn btn-primary navbar-btn" type="button"  href="">Login</a>   ####  LOGIN BUTTON ON NAVBAR
        
#                   </li>
        
        
#                   &nbsp;     &nbsp;     &nbsp;    #####  THESE ARE JUST FOR SPACES BETWEEN BUTONS
                  
        
#                 </ul>
              
                
#               </div>
        
        
#         </nav>       #### END OF NAVBAR, NOW BELOW THE BODY TAG STARTS



      
    #         <div class="text-center">
      
    #         <h2> Edenthought.... A home for your thoughts. </h2>    ## CENTRE TEXT
      
    #           <br>
                
            
    #           <a class="btn btn-outline-primary" type="button"  href="">Register</a>    REGISTER BUTTON WITH LINK TO REGISTRATION PAGE
      
            
    #         </div>
      
      
    #       </body>



    #     <script src=""></script>


        
    #     <script src="https://code.jquery.com/jquery-3.3.1.min.js"  crossorigin="anonymous"></script>    ##DEFAULT JQUERY 


    #     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"  ####  THESE ARE FOR MAKING THE NAV BAR RESPONSIVE, LIKE ON MINIMIZING THE WINDOW
                                                                                                ####  THREE BARS APPEAR AND ARRE RESPONSIVE

    #     integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"

    #     crossorigin="anonymous">

    #     </script>

    #     <script src="{% static 'js/app.js' %}"></script>


    # </html>


