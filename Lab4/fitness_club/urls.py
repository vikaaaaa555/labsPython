from django.urls import path

from . import views

urlpatterns = [
    path('fitness_club_home', views.FitnessClubHome.as_view(), name='fitness_club_home'),
    path('', views.home, name = "home"),
    path('instructors', views.InstructorsView.as_view(), name='instructors'),
    path('services', views.services, name='services'),
    path('gym_memberships', views.MembershipView.as_view(), name='gym_memberships'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('shopping_cart/<int:membership_id>/', views.shopping_cart, name='shopping_cart'),

    path('home_anonimus', views.FitnessClubHomeAnonimus.as_view(), name='home_anonimus'),
    path('instructors_anonimus', views.InstructorsAnonimusView.as_view(), name='instructors_anonimus'),
    path('services_anonimus', views.services_anonimus, name='services_anonimus'),
    path('memberships_anonimus', views.MembershipAnonimusView.as_view(), name='memberships_anonimus'),

]