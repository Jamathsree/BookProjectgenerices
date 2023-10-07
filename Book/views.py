from django.shortcuts import render
from rest_framework import generics
from .models import Author,Book
from.serializer import Authorserializer,Bookserializer

# Create your views here.
class AuthorlistView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserializer

class BooklistView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer




