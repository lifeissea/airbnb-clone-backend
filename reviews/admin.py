from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
    )
