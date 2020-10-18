from django.shortcuts import render
from insta.models import Post
from django.views.generic import TemplateView, ListView

# Create your views here.

class PostListView(ListView):
    template_name = 'post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'
