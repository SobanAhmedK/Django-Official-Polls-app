from django.shortcuts import render
from .models import question,choice
from django.http import HttpResponse,HttpRequest,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
      template_name="polls/index.html"
      context_object_name="questions_sorted_as_latest"

      def get_queryset(self):
          return question.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')[:5]


class DetailView(generic.DetailView):
    model = question
    template_name = "polls/details.html"

    def get_queryset(self):
        return question.objects.filter(publication_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context['was_published_recently'] = question.was_published_recently()
        return context
# class DetailView(generic.DetailView):
#     model=question
#     template_name="polls/details.html"
#     def get_queryset(self):
#           return question.objects.filter(publication_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model=question
    template_name="polls/results.html"
          
def vote(request:HttpRequest, question_id:int):
    Question:question=get_object_or_404(question,pk=question_id)
    try:
        choice_selected = get_object_or_404(choice, pk=request.POST["choice"])
    except(KeyError,choice.DoesNotExist):
        return render(request , "polls/details.html",{"question" : Question, "error_message" : "You didn't selected a choice"},)
    else:
        choice_selected.votes+=1
        choice_selected.save()
    return HttpResponseRedirect(reverse("polls:result", args=(Question.id,)))

