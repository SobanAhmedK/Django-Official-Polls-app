from django.shortcuts import render
from .models import question
from django.http import HttpResponse,HttpRequest



def index(request):
    questions_sorted_as_latest = question.objects.order_by("publication_date")
    questions = ','.join(q.question_text for q in questions_sorted_as_latest)
    return HttpResponse(questions)

def details(request:HttpRequest, question_id:int):
    return HttpResponse(f"This is the detail page of question {question_id}.")

def result(request:HttpRequest, question_id:int):
    return HttpResponse(f"This is the result page of question {question_id}.")

def vote(request:HttpRequest, question_id:int):
    return HttpResponse(f"This is the vote page of question {question_id}.")