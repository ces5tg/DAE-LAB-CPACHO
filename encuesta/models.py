from django.db import models

# Create your models here.
class Pregunta(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre