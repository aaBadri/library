from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from books.models import Book


# Create your views here.
class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
