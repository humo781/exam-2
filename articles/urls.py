from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('detail/<int:pk>/', views.article_detail, name='detail'),
    path('category/<str:category>/', views.articles_by_category, name='articles_by_category'),
    path('create/', views.article_create, name='create'),
]
# Done