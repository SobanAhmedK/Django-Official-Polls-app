from django.urls import path

from . import views
app_name="polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/" , views.DetailView.as_view() , name="details"),
    path("<int:pk>/result" , views.ResultView.as_view() , name="result"),
    path("<int:question_id>/vote" , views.vote , name="vote"),
    path("contact/", views.contact , name="contact"),
    path("about/", views.about , name="about"),
    path('create/', views.CreateView.as_view(), name='create')
]