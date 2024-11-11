from django.urls import path, include  # Add include here
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Am/', views.index, name='index'),
    path('update_theme/', views.update_theme, name="update_theme"),
]

# Add the language switching pattern
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # Make sure this is correct
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
