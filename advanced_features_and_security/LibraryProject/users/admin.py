from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ['email']
    # Add the new fields to the fieldsets to make them editable in the admin
    # This copies the default fieldsets and adds our custom ones.
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Add the new fields to the list display
    list_display = ['email', 'is_staff', 'date_of_birth']

admin.site.register(CustomUser, CustomUserAdmin)