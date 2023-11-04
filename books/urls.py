from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.BookList.as_view(), name = 'all'),
    path('by/<username>/', views.AuthorBooks.as_view(), name='for_author'),
    path('by/<username>/<uuid:pk>/', views.book_detail, name='book_detail'),
    path('delete/<uuid:pk>/',views.DeleteBook.as_view(),name='delete'),
    path('new_book/', views.form_display_view, name='create'),
    path('save_book/', views.form_submission_view, name='save'),
    path('update/<uuid:pk>/',views.update_book,name='update'),
    path('comments/<uuid:pk>/', views.review_detail, name='review_detail'),
]
