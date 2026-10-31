from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render


def home(request):
    return render(request, 'learning/home.html')


def science(request):
    return render(request, 'learning/science.html')


def solar_system(request):
    # Serve the original interactive page in place so its source file stays untouched.
    return FileResponse(
        (settings.BASE_DIR / 'solar_system.html').open('rb'),
        content_type='text/html',
    )

# Create your views here.
