from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


# def index(request):
#     latest_question_list = Question.objects.order_by('-id')[:10]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:10]


# def question(request, question_id):
#     # try:
#     #     current_question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Net takogo voprosa")
#     current_question1 = get_object_or_404(Question, pk=question_id)
#     context = {'question': current_question1}
#     return render(request, 'polls/detail.html', context=context)


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


# def res(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     choice_quest_ls = question.choice_set.all()
#     comment = Question.objects.get(id=question_id).another_set.all()
#     context = {
#         'choice_quest_ls': choice_quest_ls,
#         'comment': comment
#     }
#     return render(request, 'polls/res.html', context)


class ResultsView(generic.DetailView):
    template_name = 'polls/res.html'
    model = Question

    # Add context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment'] =
    #     return context


def vote(request, question_id):
    question1 = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question1.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question1,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if request.POST['test'] is not '':
            comment = question1.another_set.create(char_field_empty=request.POST['test'],
                                                   name_field=request.POST['name']
                                                   )
            comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question1.id,)))
