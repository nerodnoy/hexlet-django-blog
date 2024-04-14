from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        return render(request, 'articles/index.html')

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Hello, World!')
