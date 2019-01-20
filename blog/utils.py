from django.shortcuts import render, get_object_or_404, redirect, reverse
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
        context = {self.model.__name__.lower(): obj,
                   "detail": True,
                   "admin_o": obj
                   }
        return render(request, self.link, context=context)


class ObjectCreateMixin:
    
    link = None
    form = None

    def get(self, request):
        form = self.form()           
        return render(request, self.link, context={'form': form})

    def post(self, request):
        fill_form = self.form(request.POST)
        if fill_form.is_valid():
            new_obj = fill_form.save()
            # print(new_obj)
            return redirect(new_obj)
        
        return render(request, self.link, context={'form': fill_form})

    
class ObjectUpdateMixin:

    link = None
    form = None
    model = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=obj)
        return render(request, self.link, context={"form": bound_form, "obj": obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)

        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)

        return render(request, self.link, context={"form": bound_form, "obj": obj})


class ObjectDeleteMixin:

    link = None
    model = None
    redirect_to = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.link, context={"obj": obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_to))

