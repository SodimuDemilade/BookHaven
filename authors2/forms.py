from .models import Author
from django import forms
from django.contrib.auth.forms import UserCreationForm


class AuthorCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = Author

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = 'Email Address'
