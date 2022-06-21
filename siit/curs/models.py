from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        unique_together = ("nume", "prenume")

    nume = models.CharField(max_length=50, db_index=True)
    prenume = models.CharField(max_length=50, null=True)
    an = models.IntegerField(default=1)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.nume} {self.email}"

    def afiseaza_studenti(self):
        pass

class Curs(models.Model):
    nume = models.CharField(max_length=50)
    an = models.IntegerField()