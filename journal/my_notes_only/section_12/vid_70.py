

###  CONFIGURE STATIC FILES

## AS WE HAD CONFIGURED STATIC FILES IN ELEVATE PROJECT, WE WILL DO THE SAME FOR THIS, UNDER ROOT DIRECTORY THAT IS edenthought, WE WILL 
## CREATE A NEW FOLDER AND NAME IT AS STATIC

## so as we know we have css and js folder in it

### NOW TO SETINGS.PY FILE TO CONFIGURE THE STATIC DIRECTORY

# STATICFILES_DIRS = [BASE_DIR / 'static'] ## by this we are telling django that look for static files in the 'static' directory(that we created)
                                           ## and then by this we would be able to individually acces our css and js files, whenever we need

## WRITE THE ABOVE LINE BELOW STATIC_URL IN SETTINGS.PY FILE (AS WE DID FOR ELEVATE PROJECT). WE KNOW BECAUSE OF ABOVE, WE WILL BE ABLE TO
## LINK TO OUR STATIC FILES ACCORDINGLY.
