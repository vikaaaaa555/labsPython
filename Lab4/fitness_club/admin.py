from django.contrib import admin
from .models import *

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Instructor, InstructorAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'phone_number')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Client, ClientAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'capacity')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Group, GroupAdmin)

admin.site.register(Lesson)
admin.site.register(Payment)

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Membership, MembershipAdmin)