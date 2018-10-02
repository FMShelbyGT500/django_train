from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectListMixin, ObjectDetailMixin


class PostList(ObjectListMixin, View):
    link = "blog/post_list.html"
    model = Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "blog/post_list.html", context={'posts': posts,})


class TagsList(ObjectListMixin, View):
    link = 'blog/tags_list.html'
    model = Tag


# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    link = 'blog/post_detail.html'
    model = Post


# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})


class TagDetail(ObjectDetailMixin, View):
    link = 'blog/tag_detail.html'
    model = Tag


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug=slug)
#     return render(request, 'blog/tag_detail.html', context={"tag": tag,})
