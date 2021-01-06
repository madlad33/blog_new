from django.contrib import admin
from .models import Blogpost,Categories,UserProfile
# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Categories)
admin.site.register(UserProfile)