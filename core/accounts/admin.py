# import part
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# ______________________________________________________________________

class CustomeUserAdmin(UserAdmin):
    model=User 
    list_display =('username','email','is_superuser','is_active',"is_verified")
    list_filter =('username','email','is_superuser','is_active',"is_verified")
    searching_fields=('username','email',)
    ordering=('username',)
    fieldsets = [
        ('Athentication', {"fields": ["username", "password"]}),
        ("Permissions", {"fields": ["is_staff","is_active","is_superuser","is_verified"]}),
        ("group permissions", {"fields": ["groups","user_permissions"]}),
        ("important date", {"fields": ["last_login"]}),
    ]
    add_fieldsets = [
        (None,{"classes": ["wide"],"fields": ["username", "password1","password2", "is_staff", "is_active","is_superuser","is_verified"],},),
    ]

admin.site.register(User,CustomeUserAdmin)