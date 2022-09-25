from django.contrib import admin

from pocket_book.models import PocketBook


class PocketBookAdminConfig(admin.ModelAdmin):
    list_display = ("title", "author", "amount", "time_of_occurrence",)
    search_fields = ("title", "author",)
    list_filter = ("title", 'author',)
    ordering = ('-time_of_occurrence',)

    fieldsets = (
        ("Main", {"fields": ("title", "author", 'image')}),
        ("Money", {
            "fields": ("amount",),
        }),
        ("Time", {"fields": ("created_date", 'time_of_occurrence')}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("title", "author", "image", "amount", "time_of_occurrence"),
            },
        ),
    )


admin.site.register(PocketBook, PocketBookAdminConfig)
