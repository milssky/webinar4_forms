from django.urls import path

from .views import edit_article, index



urlpatterns = [
    path('', index),
    path('<int:article_id>/edit/', edit_article),
]
