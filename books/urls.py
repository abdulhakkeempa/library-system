from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='all'),
    path('films/<int:pk>/detail', views.BookDetailView.as_view(), name='book_detail'),
    path('films/create/', views.BookCreateView.as_view(), name='book_create'),
    path('films/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('films/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]