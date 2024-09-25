from django.urls import path
from . import views


urlpatterns = [
    path('Am/', views.index, name='index')
]