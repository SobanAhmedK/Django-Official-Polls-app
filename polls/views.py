from django.shortcuts import render,redirect
from django.db.models import F
from .models import question,choice , ContactMessage
from django.http import HttpResponse,HttpRequest,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic,View
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions_sorted_as_latest"
    paginate_by = 3  

    def get_queryset(self):
        return question.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('polls:login')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form': form})
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
class ResultView(generic.DetailView):
    model=question
    template_name="polls/results.html"
    

@login_required
def vote(request, question_id):
    
    question_instance = get_object_or_404(question, pk=question_id)

    try:
     
        selected_choice = get_object_or_404(choice, pk=request.POST["choice"])
    except (KeyError, choice.DoesNotExist):
        
        return render(request, "polls/details.html", {
            "question": question_instance,
            "error_message": "You didn't select a choice.",
        })
    else:
        previous_votes = choice.objects.filter(question=question_instance, voters=request.user)
        
        for vote_instance in previous_votes:
            if vote_instance.pk != selected_choice.pk:
                vote_instance.votes = F('votes') - 1
                vote_instance.voters.remove(request.user)
                vote_instance.save()
        
        if not selected_choice.voters.filter(pk=request.user.pk).exists():
            selected_choice.votes = F('votes') + 1
            selected_choice.voters.add(request.user)
            selected_choice.save()

    return HttpResponseRedirect(reverse("polls:result", args=(question_instance.id,)))

def about(request:HttpRequest):
    return render(request , "polls/about.html")

@method_decorator(login_required, name='dispatch')
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
        
        Question = question.objects.create(
            question_text=question_text,
            publication_date=timezone.now()
        )
        
       
        for choice_text in choice_texts:
            if choice_text.strip():  
                choice.objects.create(
                    question=Question,
                    text_choice=choice_text.strip()
                )
        
        return redirect('polls:index')



def contact(request):
    error_message = None
    success_message = None
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        age = request.POST.get('age')
        message = request.POST.get('message')

        try:
            age = int(age)
        except ValueError:
            error_message = 'Please enter a valid age.'
            return render(request, 'polls/contact.html', {'error_message': error_message})

        if not (name and email and message):
            error_message = 'Please fill in all required fields.'
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                contact=contact,
                age=age,
                message=message
            )
            success_message = 'Thank you for your response!'

    return render(request, 'polls/contact.html', {'error_message': error_message, 'success_message': success_message})


def search(request:HttpRequest):
        query = request.GET.get('q')
        results = []
        
        if query:
                results = question.objects.filter(question_text__icontains=query)
        return render(request, 'polls/search_results.html', {'results': results, 'query': query})