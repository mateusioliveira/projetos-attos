from django.urls import path
from django.contrib import admin
from django.urls import include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('instagram_button/', views.instagram_button, name='instagram_button'),
    ]