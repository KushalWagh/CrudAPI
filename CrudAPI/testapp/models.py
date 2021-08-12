from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    auther_name=models.CharField(max_length=30)
    isbn=models.IntegerField()
    publisher=models.CharField(max_length=20)

class Report(models.Model):
    report_id=models.IntegerField()
    date=models.DateField()
    payment_party=models.ForeignKey(Book,on_delete=models.CASCADE,blank=True)
    discription=models.TextField()
    amount=models.IntegerField()