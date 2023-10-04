from django.shortcuts import render

diaryPosts = [
    {
        'author': 'John Cena',
        'title': 'Diary Post 1',
        'content': 'First Diary post content',
        'date_posted': 'October 3, 2023'
    },
    {
        'author': 'Randy Orton',
        'title': 'Diary Post 2',
        'content': 'Second Diary post content',
        'date_posted': 'October 3, 2023'
    }
]



def home(request):
    context = {
        'diaryPosts': diaryPosts
    }
    return render(request, 'diary/home.html', context)

def about(request):
    return render(request, 'diary/about.html', {'title': 'About'})