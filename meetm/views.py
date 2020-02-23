from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetups

def home(request):

    return render(request,'meetm/home.html')

def user_home(request):
    context = {
        'meetup': Meetups.objects.all()
    }

    return render(request,'meetm/user_home.html', context) 

def moderator_home(request):

   return render(request,'meetm/moderator_home.html')

def user_signup(request):

   return render(request,'meetm/user_signup.html')
  
def plan_meeting(request):

   return render(request,'meetm/plan_meeting.html')
  
