from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

# Vue pour lister les articles
def liste_articles(request):
    return render(request, 'courses/liste_articles.html')

# Vue pour ajouter un article
def ajouter_article(request):
    return render(request, 'courses/ajouter_article.html')
# Vue pour lister les articles
def liste_articles(request):
    articles = Article.objects.all()  # Récupère tous les articles
    return render(request, 'courses/liste_articles.html', {'articles': articles})
# Vue pour ajouter un article
def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le nouvel article
            return redirect('liste_articles')  # Redirige vers la liste des articles
    else:
        form = ArticleForm()
    return render(request, 'courses/ajouter_article.html', {'form': form})
# Vue pour supprimer un article
def supprimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # Récupère l'article ou renvoie une 404
    article.delete()  # Supprime l'article
    return redirect('liste_articles')  # Redirige vers la liste des articles
def marquer_achete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.achete = not article.achete  # Inverse l'état actuel (acheté/non acheté)
    article.save()
    return redirect('liste_articles')