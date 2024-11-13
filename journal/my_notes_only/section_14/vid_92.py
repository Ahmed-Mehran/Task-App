
### UPDATE AND USER CONTENT-- CONFIGURE TO ALLOW FILE UPLOADS

## FIRST OF ALL DO pip install pillow TO INSTALL THE pillow LIBRARY. THIS LIBRARY IS A PYHTON IMAGING LIBRARY AND THIS IS GOING TO ALLOW
## US TO UPLOAD OUR IMAGES. AS WE WOOULD BE UPLOADING PROFILE PICTURES IN THIS PROJECT. THIS LIBRARY WILL MAKE SURE, THAT WE DONT FACE ANY PROBLEMS 
## WHILE UPLOADING IMAGES

## NOW AFTER INSTALLING THE PILLOW LIBRARY, WE WILL GO TO SETTINGS.PY FILE UNDER THE STATIC URL LINE AND AS WE KNOW THAT WE HAD ADDED A 
## STATIC URL (STATICFILES_DIRS = [BASE_DIR / 'static']) WHIC GAVE DJANGO THE ACCESS OF IMPORTING OUR JS AND CSS FILES AND IMAGES FROM STATIC FOLDER . 
## BUT WE WONT BE USING THE SAME FOR PROFILE UPLOADS OR IMAGES UPLOADS. WE USE A SEPARATE STATIC URL FOR THIS KIND OF CONTENT, BECAUSE WHEN IT COMES
## TO USER UPLOADED CONTENT, THAT NEEDS TO BE STORED IN MEDIA FOLDER FOR BEST PRACTICES AND THIS STATIC URL WILL ACCESS OF A DIFFERENT NEW FOLDER CALLED
## THE media FOLDER WHICH IS ALSO UNDER THE ROOT DIRECTORY(edenthought). SO THIS FOLDER IS WHERE ALL OUR USER UPLOADED CONTENT IS GOING TO BE SENT TO AND MANAGED
## NOW FOR THIS media FOLDER WE WILL HAVE A SEPARATE STATIC URL DEFINED IN THE SETTINGS.PY I.E AND THAT IS BELOW: 

MEDIA_URL = 'media/'## This setting specifies the base URL for media files uploaded by users. When a user uploads a file, Django serves it from this URL. 
                    ## In this case, media files will be served from a URL like http://example.com/media/.

MEDIA_ROOT = BASE_DIR / 'media'## This setting defines the filesystem path where uploaded media files will be stored. BASE_DIR represents the root directory
                               ## of your Django project, and 'media' is a directory inside that root directory where the uploaded media files will be saved.

## In simpler terms, these settings configure Django to serve user-uploaded media files from a URL starting with /media/, and to store these files in a directory named 'media' within your Django project directory.

## SO NOW WE KNOW THAT WE HAVE A LINE ABOVE I.E MEDIA_URL = 'media/' WHICH SPECIFIES THE BASE URL FOR MEDIA FILES TO BE ACCESSED BY USERS. SO When a user uploads a file, Django serves it from this URL. 
# "Django serves it from this URL" means that when a user uploads a file, such as an image or a document, Django makes that file available on the website at a specific web address (URL).
# For example, if a file is uploaded, it will be stored in the "media" folder on the server (as defined by MEDIA_ROOT). Then, Django will make it accessible to users via a URL like http://example.com/media/filename. So when someone wants to
# view or download that file, they can do so by visiting the URL starting with /media/.
# In simpler terms, Django takes care of making the uploaded files available on your website using the URL that begins with /media/.
# So basically Django makes the uploaded file visible to users? and also this file be be accessed form BASE_DIR / 'media', that is the media folder. In short, Django stores the file in the media folder and provides a way for users to access it via the /media/ URL on your website.
# WITH EXAMPLE IS BELOW AND YOU WILL UNDERSTAND IT FULLY

# File Upload: When a user uploads a file (e.g., cristiano.jpeg), Django saves it in the directory defined by MEDIA_ROOT (which is BASE_DIR / 'media'). So the file is physically stored inside the media folder in your project.

# File URL: To make the file visible to users, Django provides a URL based on MEDIA_URL, which in your case is /media/. So the file cristiano.jpeg will be accessible at www.example.com/media/cristiano.jpeg.

# User Access: When someone visits the URL www.example.com/media/cristiano.jpeg, they will see the image because Django serves the file from the media folder to the web.

## NOW FOR DJANGO TO HAVE ACCESS AND KIND OF INFORMATION ABOUT THIS URL FUNCTION. WE HAVE TO REGISTER THIS IN OUR MAIN URLS.PY(NOT THE JOURNAL ONE, BUT THE ACTUAL EDENTHOUGHT ONE). SO THIS IS WHAT WE WILL ADD IN URLS.PY



from django.contrib import admin
from django.urls import path, include

from django.conf import settings ## This line imports the settings module from Django, which contains all the settings defined in the settings.py file of your Django project

from django.conf.urls.static import static ## function provided by Django to serve media files during development

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('journal.urls')),


  
]

## WE WILL CREATE A UNIQUE URL TO ACCESS OUR MEDIAL FILES

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## DETAILS OF ABOVE LINE

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): This line adds a URL pattern to the urlpatterns list. It uses the static() function provided by Django to serve media
# files during development. Here's what each part does:

# settings.MEDIA_URL: This is the URL prefix for serving media files. It's defined in the Django settings as MEDIA_URL. For example, if MEDIA_URL is set to 'media/', then media files will be served 
# at URLs like http://localhost:8000/media/filename .

# settings.MEDIA_ROOT: This is the filesystem path to the directory where media files are stored. It's defined in the Django settings as MEDIA_ROOT. For example, it could be set to something like
# BASE_DIR / 'media/', indicating that media files are stored in a directory named 'media' within your project's base directory.

# Putting it all together, this line configures Django to serve media files from the filesystem at the specified URL (MEDIA_URL) during development. This is necessary to ensure that
# media files (such as images, videos, or user uploads) are accessible via URLs when running the development server.

## WHAT IS += ABOVE IN URLS PATTERNS AND WHY WE WRITE THE WHOLE IN STATIC FUNCTION

# +=: In Python, += is an operator used for concatenating or extending lists. In this context, urlpatterns is a list that contains URL patterns for your Django project.
# By using +=, you're adding new URL patterns to the existing list.

# static(): The static() function is provided by Django to serve static files (such as CSS, JavaScript, and images) during development. It generates URL patterns for serving
# static files based on the STATIC_URL and STATIC_ROOT settings in your Django project's settings.py file. Similarly, the line you provided serves media files(MEDIAL FILES ARE NOTHING BUT FILES UPLOADED BY USES) during development.
# So, when you write urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT), you're adding URL patterns for serving media files to the existing list of URL
# patterns (urlpatterns). The static() function generates these URL patterns based on the MEDIA_URL and MEDIA_ROOT settings, allowing you to access media files via the specified URL during development.

###########  THIS WAS ALL ABOUT CONFIGURING DJANGO TO ALLOW FILE UPLOADS







