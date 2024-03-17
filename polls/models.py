from django.db import models

<<<<<<< HEAD
class question(models.Model):
    question_text = models.CharField(max_length=300)
    publication_date = models.DateField("data published")

class choice(models.Model):
    question = models.ForeignKey(to=question, on_delete = models.CASCADE)
    text_choice = models.CharField(max_length = 200)
    votes=models.IntegerField(default=0)
=======
# Create your models here.
>>>>>>> 6321f01a43f2bb00221d258b11bca221f4121fa4
