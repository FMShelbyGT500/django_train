from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name="post_list_url"), 
    path('post/<str:slug>', views.PostDetail.as_view(), name="post_detail_url"),
    path('tags/', views.TagsList.as_view(), name="tags_list_url"),
    path('tags/<str:slug>', views.TagDetail.as_view(), name="tag_detail_url")
]