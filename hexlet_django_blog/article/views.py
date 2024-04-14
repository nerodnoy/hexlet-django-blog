from django.shortcuts import render


def index(request):
    tags = ['Фрукты', 'Овощи', 'Сладости']
    return render(
        request,
        'articles/index.html',
        context={'tags': tags},
    )