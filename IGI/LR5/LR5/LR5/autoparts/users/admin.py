from django.contrib import admin

from .models import CustomUser, User

# Register your models here.
admin.site.register(User)
admin.site.register(CustomUser)
