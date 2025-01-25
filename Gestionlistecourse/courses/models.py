from django.db import models
from django.contrib.auth.models import User  # Si vous utilisez le modèle User pour l'utilisateur

class Article(models.Model):
    nom = models.CharField(max_length=200)
    quantite = models.IntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    achete = models.BooleanField(default=False)
   

    def __str__(self):
        return self.nom
