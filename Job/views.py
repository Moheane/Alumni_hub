from django.shortcuts import render
from .models import jobModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def jobSideView(request):
    context = {
        'jobs': jobModel.objects.all()
    }
    return render(request, 'blog/home.html', context)


@login_required
def jobView(request):
    context = {
        'jobs': jobModel.objects.all()
    }
    return render(request, 'Job/jobs.html', context)
