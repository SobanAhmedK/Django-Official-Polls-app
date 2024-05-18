from django.shortcuts import render,redirect
from .models import question,choice
from django.http import HttpResponse,HttpRequest,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic,View
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


def contact(request:HttpRequest):
    return render(request , "polls/contact.html")



def about(request:HttpRequest):
    return render(request , "polls/about.html")


def contact(request:HttpRequest):
    return render(request , "polls/contact.html")

class CreateView(View):
    def get(self, request: HttpRequest):
        return render(request, 'polls/create.html')

    def post(self, request: HttpRequest):
        question_text = request.POST.get('question_text')
        choice_texts = request.POST.getlist('choices')
        
        if not question_text or not choice_texts or all(not choice for choice in choice_texts):
            return render(request, 'polls/create.html', {
                'error_message': 'You must enter a question and at least one choice.',
            })
        
        # Create the new question
        Question = question.objects.create(
            question_text=question_text,
            publication_date=timezone.now()
        )
        
        # Create the choices related to this question
        for choice_text in choice_texts:
            if choice_text.strip():  
                choice.objects.create(
                    question=Question,
                    text_choice=choice_text.strip()
                )
        
        return redirect('polls:index')



