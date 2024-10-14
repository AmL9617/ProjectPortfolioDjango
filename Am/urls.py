from django.urls import path
from . import views


urlpatterns = [
    path('Am/', views.index, name='index'),
	path('update_theme/', views.update_theme, name="update_theme"),
]