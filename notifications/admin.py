from django.contrib import admin
from . models import *



@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_seen']
    list_display_links = ['id', 'user']



