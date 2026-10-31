from django.urls import path
from django.conf import settings
from django.views.static import serve

from . import views

app_name = 'learning'

urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.science, name='science'),
    path('solar-system.html', views.solar_system, name='solar_system'),
    path(
        'assets/<path:path>',
        serve,
        {'document_root': settings.BASE_DIR / 'assets'},
        name='assets',
    ),
]
