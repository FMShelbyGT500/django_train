from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


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