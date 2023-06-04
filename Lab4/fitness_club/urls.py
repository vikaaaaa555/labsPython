from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club_cards', views.club_cards, name='club_cards')
]