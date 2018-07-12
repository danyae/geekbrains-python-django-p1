from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=False)
    text = models.TextField()
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
