from django.shortcuts import render
from .models import post
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def HomePage(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def AboutPage(request):
    return render(request, 'blog/about.html')


def contactsPage(request):
    return render(request, 'blog/contacts.html')

def landingPage(request):
    return render(request, 'blog/landing.html')