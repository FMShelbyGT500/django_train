from django.urls import path, re_path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name="post_list_url"), 
    path('post/create/', views.PostCreate.as_view(), name="post_create_url"),
    # path('post/update/', views.PostUpdate.as_view(), name="post_update_url"),
    path('post/<str:slug>/', views.PostDetail.as_view(), name="post_detail_url"),
    path('post/<str:slug>/update', views.PostUpdate.as_view(), name="post_update_url"),
    path('tags/', views.TagsList.as_view(), name="tags_list_url"),
    path('tags/create/', views.TagCreate.as_view(), name="tag_create_url"),
    # path('tags/update', views.TagUpdate.as_view(), name="tag_update_url"),
    path('tags/<str:slug>/', views.TagDetail.as_view(), name="tag_detail_url"),
    path('tags/<str:slug>/update/', views.TagUpdate.as_view(), name="tag_update_url")
]