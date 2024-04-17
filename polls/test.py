import datetime
from django.test import TestCase
from polls.models import question
from django.utils import timezone
from django.test import client
from django.urls import reverse

class QuestionMoelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time =timezone.now() + datetime.timedelta(days=30)
        future_question= question(publication_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = question(publication_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = question(publication_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(time:float,question_text:str):
    question_time=timezone.now() + datetime.timedelta(days=time)
    return question.objects.create(question_text=question_text,publication_date=question_time)

class Question_index_view_tests(TestCase):

    def test_no_questions(self):
        response=self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response , "No polls!")
    
        
    def test_future_question(self):
        create_question(time=30,question_text="Future question.")
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls!")
        self.assertQuerySetEqual(response.context["questions_sorted_as_latest"], [])
        
    def test_future_question_and_past_question(self):
        question = create_question(time=-30,question_text="Past question.")
        create_question(time=30,question_text="Future question.")
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["questions_sorted_as_latest"],
            [question],
        )
        
    
    def test_two_past_questions(self):
        question1 = create_question( time=-30,question_text="Past question 1.")
        question2 = create_question(time=-5,question_text="Past question 2.")
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["questions_sorted_as_latest"],
            [question1, question2],
        )
        
class QuestionDetailViewTests(TestCase):
        def test_future_question(self):
            future_question = create_question(time=5,question_text="Future question.")
            url = reverse("polls:details", args=(future_question.id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

        def test_past_question(self):
            past_question = create_question(time=-5,question_text="Past Question." )
            url = reverse("polls:details", args=(past_question.id,))
            response = self.client.get(url)
            self.assertContains(response, past_question.question_text)