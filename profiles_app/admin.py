from django.contrib import admin
from profiles_app.models import UserProfile,ProfileFeedItem

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
