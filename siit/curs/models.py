from django.db import models

# Create your models here.
class Curs(models.Model):
    nume = models.CharField(max_length=50)
    an = models.IntegerField()

class Student(models.Model):
    class Meta:
        unique_together = ("nume", "prenume")
        ordering = ["nume", "prenume", "-an"]

    nume = models.CharField(max_length=50, db_index=True)
    prenume = models.CharField(max_length=50, null=True)
    an = models.IntegerField(default=1)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.nume} {self.email}"

    def afiseaza_studenti(self):
        pass


class Question(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return f"Question {self.text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=25)
    correct = models.BooleanField()

    def __str__(self):
        return f"Choice {self.choice_text} Question {self.question}"