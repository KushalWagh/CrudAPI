from .models import Book,Report
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields='__all__'