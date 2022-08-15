from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LibrarianLogin.as_view(), name='login'),
    path('create-account/', views.signup_view, name='signup'),
    path('my-profile/librarian/', views.profile_view, name='profile'),
    path('homepage/library/librarian/lib-dashboard/', views.homepage_view, name='homepage'),
    path('books/book-details/', views.bookslist_view, name='books'),
    path('return-book/<str:pk>/book-returned/check-status', views.returnbooks_view, name='return-book'),
    path('edit-book-info/<str:ref>/lib/edit-form/preview/', views.edit_view, name='edit-delete'),
    
    path('logout/', views.LogoutLibrarian.as_view(), name='logout'),
]