from django.db import models

from django.contrib.auth.models import User


## MODEL FOR THOUGHTS
class Thought(models.Model):

    title = models.CharField(max_length = 150)
    content = models.CharField(max_length= 400)

    date_posted = models.DateTimeField(auto_now_add=True)  

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE , null=True)   



class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True, default = 'Default.png', upload_to='media/')  ## see as we incoroporated this line "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
                                                                                                         ## in settings.py understorages, when now we will specify upload_to='media/' a folder will
                                                                                                         ## be created in S3 bucket with name as media and from now onwards(i.e after specifying 
                                                                                                         ## upload_to='media/') every profile pic will be saved to S3 bucket under media folder


    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE , null=True) 

 