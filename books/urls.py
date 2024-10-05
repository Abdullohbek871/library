from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='list'),
    path('book/<int:pk>/', views.book_detail, name='detail'),
    path('book/create/', views.create_book, name='create'),
]