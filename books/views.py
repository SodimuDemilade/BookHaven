from django.shortcuts import render
from django.views import generic
from . import models
from braces.views import SelectRelatedMixin
from authors2.models import Author
from django.urls import reverse_lazy
from books.forms import BookCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from books.models import Book
from books.forms import BookUpdateForm

# Create your views here.

class BookList(generic.ListView):
    model = models.Book


class AuthorBooks(generic.ListView):
    model = models.Book
    template_name = "books/authors_books.html"

    def get_queryset(self):
        try:
            self.book_author = Author.objects.prefetch_related("book_set").get(
                username__iexact=self.kwargs.get("username")
            )
        except Author.DoesNotExist:
            raise Http404
        else:
            books = self.book_author.book_set.all()
            return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_author"] = self.book_author
        return context


def book_detail(request, username, pk):
    try:
        book = Book.objects.filter(author__username__iexact=username, id=pk).get()
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/book_detail.html', {'book': book})


@login_required
def form_display_view(request):
    form = BookCreateForm()
    return render(request, 'books/book_form.html', {'form': form})


@login_required
def form_submission_view(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.author = request.user.author
            new_book.save()
            return redirect('books:book_detail', username=new_book.author, pk=new_book.id)
    else:
        form = BookCreateForm()
    return render(request, 'books/book_form.html', {'form': form})

class DeleteBook(generic.DeleteView):
    model = models.Book
    success_url = reverse_lazy("books:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author_id=self.request.author.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)


def update_book(request, pk):
    book = get_object_or_404(models.Book, id=pk)
    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=pk)
    else:
        form = BookUpdateForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form, 'book': book})


def review_detail(request, pk):
    try:
        review = Review.objects.filter(id=pk).get()
    except review.DoesNotExist:
        raise Http404("Review does not exist")
    return render(request, ' books/review_detail.html', {'review': review})

# def view_comment_view()
