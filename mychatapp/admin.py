from django.contrib import admin
from .models import Profile, Friend, ChatMessage

# Register your models here.
admin.site.register([Profile, Friend, ChatMessage])