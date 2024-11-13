from django.contrib import admin

from .models import Thought, Profile

admin.site.register(Thought)  ## NOW THE MOEDL IS REGISTER AND VIEWABLE ON DJANGO ADMIN PANEL

admin.site.register(Profile)