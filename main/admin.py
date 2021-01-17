from django.contrib import admin
from .models import Contact, Discussion, Message
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['from_username', 'to_username']
# admin.site.register(Message)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['username']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['user1', 'user2']
