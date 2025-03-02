from django.db import models
from django.utils import  timezone
from datetime import timedelta
from django.contrib import admin

class question(models.Model):
    question_text = models.CharField(max_length=300)
    publication_date = models.DateField("data published")
    
    def __str__(self) -> str:
        return self.question_text
    
    # def was_published_recently(self)->bool:
    #     time_now = timezone.now()
    #     return time_now - datetime.timedelta(days=1) <=self.publication_date <= time_now
    @admin.display(
        boolean=True,
        ordering="publication_date",
        description="Published recently?",
    )
    def was_published_recently(self) -> bool:
        time_now = timezone.now().date()  # Convert to datetime.date object
        return time_now - timedelta(days=1) <= self.publication_date <= time_now

from django.contrib.auth.models import User

class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, blank=True)  # Track users who voted for this choice

    def __str__(self):
        return self.text_choice
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

