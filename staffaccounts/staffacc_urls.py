from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='staff_login'),
    path('create-account/', register, name='register'),
    path('logout', logout, name='logout'),
    path('homepage/<str:pk>/', homepage, name='home'),
    path('add-a-book-record/', add_book_record, name='add_record'),
    path('search-for-a-book/', search_for_a_book, name='search'),
    path('borrow-book/', borrow_book, name='borrow'),

]