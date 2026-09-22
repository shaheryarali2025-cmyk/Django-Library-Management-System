from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home Page
    path('books/', views.book_list, name='book_list'),  # Book List Page
    path('add_book/', views.add_book, name='add_book'),  # Move "Add Book" under "books/"
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
