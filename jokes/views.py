from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


from .models import Post


class JokesListView(ListView):
    model = Post
    template_name = "home.html"


class JokesDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class JokesCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["user","question","answer" , "created_at", "update_at"]


class JokesUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["question","answer" , "created_at", "update_at"]


class JokesDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
