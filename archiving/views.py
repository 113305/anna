from django.shortcuts import render
from .models import Work

def index(request):
    return render(request, 'archiving/index.html', {})

def works(request):
    works = Work.objects.all()
    return render(request, 'archiving/works.html', {'works' : works})

def contact(request):
    return render(request, 'archiving/contact.html', {})

def profile(request):
    return render(request, 'archiving/profile.html', {})
