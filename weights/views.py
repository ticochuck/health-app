from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Post


def home(request):
    context = {
        'data': Post.objects.all()
    }
    return render(request, 'weights/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'weights/home.html'
    context_object_name = 'data'
    ordering = ['-date_posted'] # to post newer posts on top


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['weight', 'date_posted', 'notes']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['weight', 'date_posted', 'notes']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def about(request):
    return render(request, 'weights/about.html')
