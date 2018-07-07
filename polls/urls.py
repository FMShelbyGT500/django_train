from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('curr_poll=<int:question_id>/', views.question, name='detail'),
    # ex: /polls/5/results/
    path('curr_poll=<int:question_id>/results/', views.res, name='results'),
    # ex: /polls/5/vote/
    path('curr_poll=<int:question_id>/vote/', views.vote, name='vote'),
]