from django.shortcuts import render
from django.http import HttpRequest
from .models import Profile, Profiles
# Create your views here.


def home(request):
    profiles = Profile.objects.all()
    profile = Profiles.objects.all()
    context = {
        'profiles': profiles,
        'profile': profile,
    }
    return render(request, 'portfolio/home.html',  context=context)
