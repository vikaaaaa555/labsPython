from django.shortcuts import render


def index(request):
    return render(request, 'fitness_club/index.html')

def gym_memberships(request):
    return render(request, 'fitness_club/gym_membership.html')

def instructors(request):
    return render(request, 'fitness_club/instructors.html')

def services(request):
    return render(request, 'fitness_club/services.html')

