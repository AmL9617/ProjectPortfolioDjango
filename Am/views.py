from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Home, About, Profile, Category, Skills, Project
import json
from django.utils.translation import gettext 
from django.utils.translation import get_language

# Create your views here.
def update_theme(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        theme = data.get('theme')
        print(theme)
        request.session['theme'] = theme  # Store the theme in the session
        return JsonResponse({'status': 'success', 'message': 'Theme updated successfully'})
    
def index(request):
    current_lang = get_language()
    theme = request.session.get('theme', 'lightMode.css')

    home = Home.objects.language(current_lang).latest('updated')
    about = About.objects.language(current_lang).latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.language(current_lang).all()
    projects = Project.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects,
        'theme': theme, 
    }

    return render(request, 'index.html', context)

def some_view(request):
    # Get theme from session or user profile
    theme = request.session.get('theme', 'lightMode.css')  # Default to light mode
    # If using user profile:
    # theme = request.user.profile.theme if request.user.is_authenticated else 'lightMode.css'

    return render(request, 'index.html', {'theme': theme})