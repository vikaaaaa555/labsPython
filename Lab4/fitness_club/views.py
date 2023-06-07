import random
import requests
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import *


class FitnessClubHome(ListView):
    model = Group
    template_name = 'fitness_club/index.html'
    context_object_name = 'groups'
    ordering = ['name']


# def index(request):
#     groups = Group.objects.order_by('name')
#
#     context = {
#         'groups': groups,
#     }
#     return render(request, 'fitness_club/index.html', context)

class MembershipView(ListView):
    model = Membership
    template_name = 'fitness_club/gym_membership.html'
    context_object_name = 'memberships'

# def gym_memberships(request):
#     #memberships = Membership.objects.all()
#     memberships = Membership.objects.order_by('name')
#     #mem = Membership.objects.all()
#
#     context = {
#         'memberships': memberships,
#         #'mem': mem
#     }
#
#     return render(request, 'fitness_club/gym_membership.html', context)

class InstructorsView(ListView):
    model = Instructor
    template_name = 'fitness_club/instructors.html'
    context_object_name = 'instructor'
    ordering = ['name']

# def instructors(request):
#     instructor = Instructor.objects.order_by('name')
#
#     context = {
#         'instructor': instructor
#     }
#
#     return render(request, 'fitness_club/instructors.html', context)



def services(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']

    response = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = response.json()
    random_fact = random.choice(facts)

    context = {
        'image_url': image_url,
        'random_fact': random_fact
    }

    return render(request, 'fitness_club/services.html',  context)

def shopping_cart(request, membership_id):
    memberships = Membership.objects.order_by('name')
    pushcase = Membership.objects.get(pk=membership_id)
    return render(request, 'fitness_club/shopping_cart.html', {'memberships':memberships, 'pushcase': pushcase})

def home(request):
    return render(request,"fitness_club/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

