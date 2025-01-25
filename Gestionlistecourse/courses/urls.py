from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('ajouter/', views.ajouter_article, name='ajouter_article'),
]
