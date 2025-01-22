from django.contrib import admin
from .models import Article  # Assurez-vous d'importer le modèle correctement

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'quantite', 'date_ajout')  # Ces champs doivent exister dans le modèle
    search_fields = ('nom',)
