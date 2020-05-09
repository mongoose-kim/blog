from django.shortcuts import render

# Create your views here.
from .models import Blog

def home(request):
    mytext = Blog.objects
    return render(request, 'home.html', {'powerblog' : mytext})
