from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    file = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={'accept': 'application/pdf'})
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'available', 'file']
