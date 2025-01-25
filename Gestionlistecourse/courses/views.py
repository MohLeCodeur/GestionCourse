from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect


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