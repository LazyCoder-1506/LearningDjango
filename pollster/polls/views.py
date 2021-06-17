from django.http.response import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question, Choice

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404('Question does not exist')
  return render(request, 'polls/detail.html', {'questino': question})

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})