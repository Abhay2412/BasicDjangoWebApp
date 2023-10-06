from django.shortcuts import render
from .models import DiaryPost


def home(request):
    context = {
        'diaryPosts': DiaryPost.objects.all()
    }
    return render(request, 'diary/home.html', context)

def about(request):
    return render(request, 'diary/about.html', {'title': 'About'})