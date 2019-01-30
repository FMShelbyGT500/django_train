from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']  # можно '__all__' для всех полей

        widgets = {
            "title": forms.TextInput(attrs={
                'class': "form-control pretty-move-inp",
                'placeholder': "Enter the title"
            }),

            "slug": forms.TextInput(attrs={
                'class': "form-control mb-2 pretty-move-inp",
                'placeholder': "Enter the slug"
            })
        }

    def clean_slug(self):
        cln_slug = self.cleaned_data["slug"].lower()
        
        if cln_slug == 'create':
            raise ValidationError(_("you cannot name a slug as 'create'"))
        if Tag.objects.filter(slug__iexact=cln_slug):
            raise ValidationError(_(f'"{cln_slug}" slug already exist'))

        return cln_slug    

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title = self.cleaned_data['title'],
    #         slug = self.cleaned_data['slug']
    #     )

        # return new_tag

    
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter the title"
            }),

            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the slug"
            }),

            "body": TinyMCE(
            attrs={
                "class": "form-control pretty-move-inp",
                "style": "height:150px",                
            },
            mce_attrs={
                "class": "form-control pretty-move-inp",
                "style": "height:150px",
            }),

            "tags": forms.SelectMultiple(attrs={
                "class": "form-control mb-2",
                "size": "8"
            })

        }

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()}
    # }
    
    def clean_slug(self):
        cln_slug = self.cleaned_data['slug'].lower()

        if Post.objects.filter(slug__iexact=cln_slug):
            raise ValidationError(_("current slug already exist"))
        if cln_slug == "create":
            raise ValidationError(_("you cannot name a slug as 'create'"))

        return cln_slug


# class Temo(forms.Form):
    # cont = forms.
