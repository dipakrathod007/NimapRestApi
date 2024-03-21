from django.contrib import admin
from .models import Client, Project,User

# Register your models here.

@admin.register(User)
@admin.register(Client)
@admin.register(Project)

class UserAdmin(admin.ModelAdmin):
    list_userdisplay=['id','user_name']

class ClientAdmin(admin.ModelAdmin):
    list_display1 = ['id','client_name','created_at','created_by','updated_at']

class ProjectAdmin(admin.ModelAdmin):
    list_display2 = ['id','project_name','created_at','created_by','client']