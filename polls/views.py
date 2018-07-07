from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-id')[:10]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def question(request, question_id):
    # try:
    #     current_question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Net takogo voprosa")
    current_question1 = get_object_or_404(Question, pk=question_id)
    context = {'question': current_question1}
    return render(request, 'polls/detail.html', context=context)


def res(request, question_id):
    choice_quest_ls = Question.objects.get(id=question_id).choice_set.all()
    context = {
        'choice_quest_ls': choice_quest_ls
    }
    return render(request, 'polls/res.html', context)


def vote(request, question_id):
    return HttpResponse("You're voting on question aa %s." % question_id)



