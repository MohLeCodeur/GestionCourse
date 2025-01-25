from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('ajouter/', views.ajouter_article, name='ajouter_article'),
     path('supprimer/<int:article_id>/', views.supprimer_article, name='supprimer_article'),
     path('marquer_achete/<int:article_id>/', views.marquer_achete, name='marquer_achete'),
]
