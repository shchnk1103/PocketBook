from django.contrib import admin
from my_user.models import MyUser
from django.contrib.auth.admin import UserAdmin
from django import forms


class AdminConfig(UserAdmin):
    list_display = ("email", "username", "is_superuser", "is_active")
    search_fields = ("username", "first_name", "email", )
    list_filter = ("email", "is_superuser", "is_active")
    ordering = ('-start_date',)

    fieldsets = (
        (None, {"fields": ("email", "username", "first_name", "password")}),
        ("Permissions", {
         "fields": ("is_active", "is_staff", "is_superuser",),
         }),
        ("Personal", {"fields": ("about", )}),
    )
    formfield_overrides = {
        MyUser.about: {'widget': forms.Textarea(
            attrs={'rows': 10, 'cols': 40})}
    }

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "first_name", "last_name", "password1", "password2",
                           "is_active", "is_staff"),
            },
        ),
    )


admin.site.register(MyUser, AdminConfig)
