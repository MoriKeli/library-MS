from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.BookView.as_view()),
    path('book/<str:pk>/', views.BookDetails.as_view()),
]