from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Home, About, Profile, Category, Skills, Project
import json
from django.utils.translation import gettext 

# Create your views here.

def index(request):
	return render(request, 'base/index.html')

def update_theme(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        theme = data.get('theme')
        print(theme)
        request.session['theme'] = theme  # Store the theme in the session
        return JsonResponse({'status': 'success', 'message': 'Theme updated successfully'})
    
def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    # Skills
    categories = Category.objects.all()

    # Projects
    projects = Project.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects
    }


    return render(request, 'index.html', context)

def some_view(request):
    # Get theme from session or user profile
    theme = request.session.get('theme', 'lightMode.css')  # Default to light mode
    # If using user profile:
    # theme = request.user.profile.theme if request.user.is_authenticated else 'lightMode.css'

    return render(request, 'index.html', {'theme': theme})