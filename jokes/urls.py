from django.urls import path
from .views import (
    JokesListView,
    JokesDetailView,
    JokesCreateView,
    JokesUpdateView,
    JokesDeleteView, 
    SignUpView,
)

urlpatterns = [
    path("post/new/", JokesCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", JokesDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", JokesUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", JokesDeleteView.as_view(), name="post_delete"), 
    path("/", JokesListView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),

]
