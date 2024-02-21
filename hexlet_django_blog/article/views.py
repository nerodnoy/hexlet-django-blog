from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    title = 'Articles'
    description = 'Project by nerodnoy'
    return render(
        request,
        'articles.html',
        context={
            'title': title,
            'description': description
        }
    )
