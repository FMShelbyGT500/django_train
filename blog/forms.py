from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    title.widget.attrs.update({
        'class': "form-control pretty-move-inp",
        'placeholder': "Enter the title"
    })
    slug.widget.attrs.update({
        'class': "form-control mb-2 pretty-move-inp",
        'placeholder': "Enter the slug"
    })

    def clean_slug(self):
        cln_slug = self.cleaned_data["slug"]
        
        if cln_slug == 'create':
            raise ValidationError('can`t be that')

        return cln_slug    

    def save(self):
        new_tag = Tag.objects.create(
            title = self.cleaned_data['title'],
            slug = self.cleaned_data['slug']
        )

        return new_tag