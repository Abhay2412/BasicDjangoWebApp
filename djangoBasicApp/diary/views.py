from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import DiaryPost


def home(request):
    context = {"diaryPosts": DiaryPost.objects.all()}
    return render(request, "diary/home.html", context)


class DiaryPostListView(ListView):
    model = DiaryPost
    template_name = "diary/home.html"
    context_object_name = "diaryPosts"
    ordering = ["-date_posted"]


class DiaryPostDetailView(DetailView):
    model = DiaryPost


class DiaryPostCreateView(LoginRequiredMixin, CreateView):
    model = DiaryPost
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DiaryPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryPost
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        diaryPost = self.get_object()
        if self.request.user == diaryPost.author:
            return True
        return False


class DiaryPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DiaryPost
    success_url = "/"

    def test_func(self):
        diaryPost = self.get_object()
        if self.request.user == diaryPost.author:
            return True
        return False


def about(request):
    return render(request, "diary/about.html", {"title": "About"})
