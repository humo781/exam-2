from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    ctx = {'article': article}
    return render(request, 'articles/detail.html', ctx)

def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')
        category = request.POST.get('category')
        if title and short_content and long_content and author and category:
            Article.objects.create(
                title=title,
                short_content=short_content,
                long_content=long_content,
                author=author,
                category=category
            )
            return redirect('home')
    return render(request, 'articles/add-post.html')

def articles_by_category(request, category):
    articles = Article.objects.filter(category=category)
    print(articles)
    if articles.exists():
        print("Maqolalar mavjud")
    else:
        print("Maqolalar yo'q")
    ctx = {'articles': articles, 'category': category}
    return render(request, 'articles/articles-by-category.html', ctx)


def article_delete(request):
    pass