from django.shortcuts import render
from .models import Book,Report
from rest_framework import generics
from .serializer import BookSerializer,ReportSerializer

class BookList(generics.ListCreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report
    serializer_class = ReportSerializer