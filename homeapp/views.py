from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

def home(request):
    post=Post.objects.all()
    return render(request, 'homeapp/info.html', {'posts':post})

@login_required
def profile(request):
    return render(request, 'homeapp/profile.html')
