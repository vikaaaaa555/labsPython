from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('instructors', views.instructors, name='instructors'),
    path('services', views.services, name='services'),
    path('gym_memberships', views.gym_memberships, name='gym_memberships'),
]