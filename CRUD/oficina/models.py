from django.db import models

class oficina(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    nombre_corto = models.CharField(verbose_name="Nombre Corto", max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.nombre_corto}"

