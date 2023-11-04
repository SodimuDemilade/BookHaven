from django.shortcuts import render
from django.views import generic
from .models import Author
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from . import forms

# Create your views here.
class CreateAccount(generic.CreateView):
    form_class = forms.AuthorCreateForm
    success_url = reverse_lazy('login')
    template_name = 'authors2/signup.html'


class CustomLoginView(LoginView):
    template_name = 'authors2/login.html'

    def get_success_url(self):
        return reverse_lazy('books:create')


class AuthorList(generic.ListView):
    model = Author


def author_detail(request, username):
    try:
        author = Author.objects.filter(username=username).get()
    except Book.DoesNotExist:
        raise Http404("Author does not exist")
    return render(request, 'authors2/author_detail.html', {'author': author})
