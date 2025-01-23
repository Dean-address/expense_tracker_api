from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    list_display = [
        "email",
        "username",
        "is_admin",
        "is_active",
        "is_staff",
    ]
    list_filter = ["is_admin", "is_active", "is_staff"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["username"]}),
        ("Permissions", {"fields": ["is_admin", "is_active", "is_staff"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"],
            },
        ),
    ]

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(CustomUser, CustomUserAdmin)
