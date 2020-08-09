from django.contrib import admin
from .models import User, Like , Comment ,Tweet


# Register your models here.
admin.site.register(User)
admin.site.register(Like)
admin.site.register(Tweet)
admin.site.register(Comment)