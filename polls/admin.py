from django.contrib import admin
from .models import question,choice

class ChoiceInline(admin.TabularInline):  #can be admin.StackInLine
    
    model =  choice
    extra=3
    
class QuestionAdmin(admin.ModelAdmin):
    fields = ["publication_date" , "question_text"]
    inlines=[ChoiceInline]
    list_display=("question_text", "publication_date", "was_published_recently")
    list_filter=["publication_date"]
    search_fields=["question_text"]
admin.site.register(question,QuestionAdmin)
admin.site.register(choice)
