from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)

from .models import Post

# Create your views here.

# posts = [{
#     'author': 'timon',
#     'title': 'timon and pumma',
#     'content': 'this is for anime network',
#     'date_posted': 'August 28, 2018'
# }, {
#     'author': 'pumba',
#     'title': 'pumma',
#     'content': 'this is for anime network. and you gone love it',
#     'date_posted': 'August 20, 2018'
# }]

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# class PostListView(ListView):
#     model = Post
#     # <app>/<model>_<viewtype>.html
#     template_name = 'blog/home.html'

#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     # ?page=4
#     paginate_by = 2
#     pass

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

# class PostDetailView(DetailView):
#     model = Post
#     # <app>/<model>_<viewtype>.html
#     # context_object_name = 'post'
#     template_name = "blog/detail.html"

class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    # <app>/<model>_<viewtype>.html
    # context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    # <app>/<model>_<viewtype>.html
    # context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    success_url = '/'

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
