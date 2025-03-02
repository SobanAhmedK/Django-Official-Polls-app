from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name="polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path("<int:pk>/" , views.DetailView.as_view() , name="details"),
    path("<int:pk>/result/" , views.ResultView.as_view() , name="result"),
    path("<int:question_id>/vote/" , views.vote , name="vote"),
    path("contact/", views.contact , name="contact"),
    path("about/", views.about , name="about"),
    path('create/', views.CreateView.as_view(), name='create'),
    path('search/', views.search, name='search')
]