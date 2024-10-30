from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff", "is_superuser")
    ordering = ("email",)

    # Exclude username field and include only the fields defined in your custom User model
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "instituicao")}),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
                "description": "Checkboxes control permissions",
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "instituicao",
                ),
            },
        ),
    )

    filter_horizontal = ()
    filter_vertical = ()
    readonly_fields = ()
