
######   CREATE AND REGISTER A PROFILE MODEL

## SEE ONE MIGHT THINK WHY DO WE NEED THIS, WHY ISNT IT PROVIDED BY DJANGO AS DEFAULT. IF YOU REMMEBER WHEN WE CREATED/registered USERS WE USED A SPECIAL
## INBUILT MODULE PRVIDED BY DJANGO CALLED THE UserCreationForm WHICH CONVERTED THE DFAULT USER MODEL TO FORM, AND IT HAD THE CAPABILITIES TO 
## CREATE FORM WITH FIELDS AS USERNAME, PASSSWORD, EMAIL, BUT WE DIDNT GET A DEFAULT FIELD FOR UPLOADING PROFILE IMAGES WITH THE DEFAULT USER MODEL.
## SO NOW WE HAVE TO ADD IN SOME FUNCTIONALITY, SO THAT WE CAN ADD A PRFILE IMAGE. 

## WHAT WE WIL DO IS WE WILL FIRST CREATE ANOTHER MODEL/DATABASE TABLE(RELATED TO THIS IMAGE FIELDS) AND THEN LINK THAT MODEL TO USER(DEFAULT DJANGO MODEL) MODEL 
## AND THEN MAKE USE OF FOREIGN KEY, THAT BINDS THAT USER MODEL TO THE PARTICULAR MODEL(THAT WE CREATE) OR WE AN SAY BINDS THE USER TO A PROFILE PICTURE

#### SO WE WILL FIRST HEAD ONTO MODELS.PY

#########################   MODELS.PY

## SEE ABOVE AS THOUGHT MODEL IS LINKED TO USER MODEL BY A FOREIGN KEY (user) WE WILL USE THE SAME LOGIC FOR LINKING THIS MODEL TO USER MODEL 

class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True, default = 'Default.png') #(null=True and blank=True), meaning users can choose not to upload a profile picture. 

## data type is going to be Image field, null=True allows our objects to have a null value in this database table(we dont need this but we can write this)
## blank=True allows us to have a null value in Form, suppose we dont upload any profile picture and want to leave it blank, this is for that
## default = '' provides an opportunity to set a default profile picture for our users. see by use of thiS DeFault,  django is going to know where to look for these
## images and files and default location is set automatically to Media_root(that we defind in settings.py) WHICH IS STATIC FUNCTION FOR media FOLDER. BUT HOW IS THIS 
## POSSIBLE HOW DOES THE DEFAULT AUTOMATICALLY LOOKS UP AND FINDS THE STATIC FUNCTION/URL OF media folder. BELOW THAT IS EXPLAINED

# In Django models, the ImageField stores the path to an image file relative to the MEDIA_ROOT setting in your project's settings.py. When you set default='' for the 
# profile_pic field, it means that by default, this field will be empty (i.e., no image selected) unless explicitly provided.

# If you want to set a default image for the profile_pic field, you should specify the path to the default image file instead of an empty string. For example:

# profile_pic = models.ImageField(null=True, blank=True, default='default_profile_pic.jpg')

# In this case, Django will look for the default_profile_pic.jpg file relative to the MEDIA_ROOT directory. If no image is uploaded for a particular Profile instance, it will use this default image.

# SO the ImageField in Django is responsible for storing references to image files. When an image is uploaded through a form and associated with an ImageField, Django handles storing the image file on the 
# server and updating the database with the file's path relative to the MEDIA_ROOT directory. This path allows Django to retrieve the image when it needs to display it on a webpage or access it programmatically.
#  If no image is uploaded for a particular instance of the model, the ImageField can be configured with a default value to display a placeholder image or some other default content.

## IN THE Default = '', we will for now reference the image in media folder. so for now it will act as a default picture(which cna be later changed), so default = 'Default.png'

## NOW AFTER THIS WE WILL DEFINE THE FOREIGN KEY RELATION SHIP BETWEEN THIS AND THE USER MODEL, SO WE CAN COPY THE user FOREIGN KEY ATTRIBUTE FROM ABOVE THOUGHT MODEL

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE , null=True) 

    ## THE IDEA OF USING A RELATINSHIP KEY IS THAT WHENEVER WE CREATE A NEW USER, WE WILL AUTOMATICALLY CREATE A NEW PROFILE OBJECT, WHICH IS GOING TO LINKTO THAT PARTICULAR
    ## USER VIA THE FOREIGN KEY


    ### NOW WE WILL DO THE MIGRATION PART AS NEW MODEL IS CREATED  AND HEAD ONTO ADMIN.PY TO REGISTER THE MODEL TO BE ABLE TO VIEW IT IN DASHBOARD (admin.site.register(Profile))



