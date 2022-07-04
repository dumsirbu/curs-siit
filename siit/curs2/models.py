from django.db import models

# Create your models here.

class ModelExemplu(models.Model):
    class Meta:
        verbose_name_plural = "Modele Exemplu"
    nume = models.CharField(max_length=100)