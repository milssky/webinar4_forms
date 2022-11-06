from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArticleForm
from .models import Article


def index(request):
    articles = Article.objects.all()
    # form = ArticleForm(request.POST or None)
    # form.save()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        form.save()
        return redirect('index')
    form = ArticleForm()
    return render(request, 'articles/article.html', {
        'articles': articles,
        'form': form
    })


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == "POST":
        form.save()
    print("Сохранено через edit_article")
    articles = Article.objects.all()
    return render(request, 'articles/article.html', {
        'articles': articles,
        'form': form
    })
