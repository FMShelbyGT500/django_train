from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index_url'),
    path('curr_poll=<int:pk>/', views.DetailView.as_view(), name='detail_url'),
    path('curr_poll=<int:pk>/results/', views.ResultsView.as_view(), name='results_url'),
    path('curr_poll=<int:question_id>/vote/', views.vote, name='vote_url'),
]