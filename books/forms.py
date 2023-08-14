from django import forms
from .models import Author, Tags, Books

# Create the form class.

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author

class TagForm(forms.ModelForm):
    class Meta:
      model = Tags

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["name", "author", "stock", "genre", "per_day_charge"]
