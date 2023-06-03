from django.urls import path

from fitness_club.tests import views

urlpatterns = [
    path("", views.index, name="index"),
]