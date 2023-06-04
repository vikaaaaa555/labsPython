from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'fitness_club/index.html')

def club_cards(request):
    return HttpResponse("<h4>Info about club cards<h4>")