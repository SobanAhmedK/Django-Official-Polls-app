from django.shortcuts import render
from .models import question
from django.http import HttpResponse,HttpRequest,Http404
from django.template import loader
from django.shortcuts import render


def index(request):
    questions_sorted_as_latest = question.objects.order_by("publication_date")
    template=loader.get_template("polls/index.html")
    context={"questions_sorted_as_latest":questions_sorted_as_latest}
    return HttpResponse(template.render(context ,request))

def details(request:HttpRequest, question_id:int):
    try:
        Question = question.objects.get(pk=question_id)
    except question.DoesNotExist(Question):
        raise Http404("Question does not exist")
    return render(request ,"polls/details.html" , {"question" : Question} )
        

def result(request:HttpRequest, question_id:int):
    return HttpResponse(f"This is the result page of question {question_id}.")

def vote(request:HttpRequest, question_id:int):
    return HttpResponse(f"This is the vote page of question {question_id}.")