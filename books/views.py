from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Books


class BookBaseView(View):
    model = Books
    fields = '__all__'
    success_url = reverse_lazy('books:all')


class BookListView(BookBaseView, ListView):
    """View to list all films.
    Use the 'book_list' variable in the template
    to access all Book objects"""


class BookDetailView(BookListView, DetailView):
    """View to list the details from one book.
    Use the 'book' variable in the template to access
    the specific book here and in the Views below"""


class BookCreateView(BookBaseView, CreateView):
    """View to create a new book"""


class BookUpdateView(BookBaseView, UpdateView):
    """View to update a book"""


class BookDeleteView(BookBaseView, DeleteView):
    """View to delete a book"""