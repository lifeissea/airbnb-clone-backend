from django.urls import path
from .views import Perks, PerksDetails

urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerksDetails.as_view()),
]
