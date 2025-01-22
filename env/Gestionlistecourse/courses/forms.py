from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom', 'quantite']  # Assurez-vous que ces champs existent dans le modèle
