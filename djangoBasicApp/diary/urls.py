from django.urls import path
from .views import (
    DiaryPostListView,
    DiaryPostDetailView,
    DiaryPostCreateView,
    DiaryPostUpdateView,
    DiaryPostDeleteView,
)
from . import views

urlpatterns = [
    path("", DiaryPostListView.as_view(), name="diary-home"),
    path("diaryPost/<int:pk>/", DiaryPostDetailView.as_view(), name="diaryPost-detail"),
    path("diaryPost/new/", DiaryPostCreateView.as_view(), name="diaryPost-create"),
    path(
        "diaryPost/<int:pk>/update/",
        DiaryPostUpdateView.as_view(),
        name="diaryPost-update",
    ),
    path(
        "diaryPost/<int:pk>/delete/",
        DiaryPostDeleteView.as_view(),
        name="diaryPost-delete",
    ),
    path("about/", views.about, name="diary-about"),
]
