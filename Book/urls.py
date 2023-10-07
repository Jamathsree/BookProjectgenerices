from .import views
from django.urls import path

urlpatterns = [
    path('jamath/',views.AuthorlistView.as_view()),
    path('Author/<int:pk>',views.AuthorDetailView.as_view()),
    path('book/',views.BooklistView.as_view()),
    path('Book/<int:pk>',views.BookDetailView.as_view()),
]