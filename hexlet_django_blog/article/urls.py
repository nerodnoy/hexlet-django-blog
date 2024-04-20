from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.redirect_to_article, name='home'),
    path('articles/<str:tags>/<int:article_id>/', views.IndexView.as_view(), name='article'),
]