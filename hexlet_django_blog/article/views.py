from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect


class IndexView(View):
    def get(self, request, tags=None, article_id=None):
        article_text = f"Статья номер {article_id}. Тег {tags}"
        return render(request, 'articles/index.html', {'article_text': article_text})

    def redirect_to_article(request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))
