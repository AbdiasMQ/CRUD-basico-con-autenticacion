from django.db import models
from oficina.models import oficina as Oficina

class persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    apellido = models.CharField(verbose_name="Apellido", max_length=100)
    edad = models.IntegerField(verbose_name="Edad")
    oficina = models.ForeignKey(Oficina,
                                on_delete=models.CASCADE,
                                related_name='personas',
                                null=True, 
                                blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.edad} - {self.oficina}"