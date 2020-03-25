from django.shortcuts import render
from django.conf import settings

# Create your views here.

# pages/views.py

from django.http import HttpResponse

def homePageView(request):
        print(settings.BASE_DIR)
        return HttpResponse('Hello, World!  My precious <br><img src="https://upload.wikimedia.org/wikipedia/en/e/e0/Gollum.PNG">')
