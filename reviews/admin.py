from django.contrib import admin
from .models import Review


class RatingFilter(admin.SimpleListFilter):

    title = "Filter by Ratings!"

    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad"),
            ("good", "Good"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, requset, reviews):
        solt_rating = self.value()
        if solt_rating == "bad":
            return reviews.filter(rating__lt=3)
        elif solt_rating == "good":
            return reviews.filter(rating__exact=3)
        elif solt_rating == "awesome":
            return reviews.filter(rating__gt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        RatingFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
