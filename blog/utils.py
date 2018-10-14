from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostForm, TagForm


class ObjectListMixin:
    link = None
    model = None

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.link, context={self.model.__name__.lower()+'s': obj})


class ObjectDetailMixin:
    link = None
    model = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.link, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    
    link = None
    form = None

    def get(self, request):        
        form = self.form()
        return render(request, self.link, context={'form': form})

    def post(self, request):
        bound_form = self.form(request.POST)
        print(bound_form)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        
        return render(request, self.link, context={'form': bound_form})