from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name="post_list_url"), 
    path('post/<str:slug>', views.post_detail, name="post_detail_url"),
]