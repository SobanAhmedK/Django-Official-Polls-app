from django.db import models
from django.utils import  timezone
from datetime import timedelta
import datetime

class question(models.Model):
    question_text = models.CharField(max_length=300)
    publication_date = models.DateField("data published")
    
    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self)->bool:
        return self.publication_date >= timezone.now() - datetime.timedelta(days=30)

class choice(models.Model):
    question = models.ForeignKey(to=question, on_delete = models.CASCADE)
    text_choice = models.CharField(max_length = 200)
    votes=models.IntegerField(default=0)

