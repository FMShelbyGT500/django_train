from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectListMixin, ObjectDetailMixin
from .forms import *


class PostList(ObjectListMixin, View):
    link = "blog/post_list.html"
    model = Post


class TagsList(ObjectListMixin, View):
    link = 'blog/tags_list.html'
    model = Tag


class PostDetail(ObjectDetailMixin, View):
    link = 'blog/post_detail.html'
    model = Post


class TagDetail(ObjectDetailMixin, View):
    link = 'blog/tag_detail.html'
    model = Tag


class TagCreate(View):
    
    def get(self, request):        
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


class PostCreate(View):

    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)

        return render(request, 'blog/post_create.html', context={'form': bound_form})

