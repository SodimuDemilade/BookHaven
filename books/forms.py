from django import forms
from .models import Book, Review


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'genre', 'price', 'content', 'contributors', 'contributors_role')

        def __init__(self, *args, **kwargs):
            super(BookCreateForm, self).__init__(*args, **kwargs)
            self.fields['authors'].required = False

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'genre', 'price', 'content', 'contributors', 'contributors_role')
