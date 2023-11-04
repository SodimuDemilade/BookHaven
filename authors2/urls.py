from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from books.views import CreateBook

app_name = 'Authors'

urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(template_name='authors2/login.html'),name='login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.CreateAccount.as_view(),name='signup'),
    path('', views.AuthorList.as_view(), name='all'),
    path('<username>/', views.author_detail, name='author_detail'),
]
