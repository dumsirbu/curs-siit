from django.db import models

# Create your models here.

class Student(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50, null=True)
    an = models.IntegerField()
    email = models.EmailField()
    telefon = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.nume} {self.email}"

class Curs(models.Model):
    nume = models.CharField(max_length=50)
    an = models.IntegerField()