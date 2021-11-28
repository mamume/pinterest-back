from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserFollowing)
admin.site.register(UserBlocked)
admin.site.register(Message)
admin.site.register(Notification)


