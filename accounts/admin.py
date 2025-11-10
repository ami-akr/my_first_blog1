from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, LinkUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('number', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'number')

    fieldsets = (
        (None, {"fields": ("email", "password", "number", "username")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "user_permissions", "picture", "bio", "first_name", "last_name")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "number", "email", "password1", "password2", "is_staff",
                "is_active", "user_permissions",
            )}
         ),
    )
    search_fields = ("number",)
    ordering = ("is_staff",)

admin.site.register(User, CustomUserAdmin)

admin.site.register(LinkUser)




