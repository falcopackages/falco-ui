from django import forms

from .models import Author
from .models import Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "birth_date")
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "published_date", "isbn", "description")
        widgets = {
            "published_date": forms.DateInput(attrs={"type": "date"}),
        }
