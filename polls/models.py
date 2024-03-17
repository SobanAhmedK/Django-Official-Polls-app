from django.db import models

class question(models.Model):
    question_text = models.CharField(max_length=300)
    publication_date = models.DateField("data published")

class choice(models.Model):
    question = models.ForeignKey(to=question, on_delete = models.CASCADE)
    text_choice = models.CharField(max_length = 200)
    votes=models.IntegerField(default=0)