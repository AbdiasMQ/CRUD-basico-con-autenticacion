from django.db import models
from oficina.models import Oficina

class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    apellido = models.CharField(verbose_name="Apellido", max_length=100)
    edad = models.IntegerField(verbose_name="Edad")
    oficina = models.ForeignKey(Oficina,
                                on_delete=models.CASCADE,
                                related_name='persona',
                                null=True, 
                                blank=True)

    
    class Meta:
        """definicion de persona."""

        verbose_name ='Persona'
        verbose_name_plural ='Personas'
        #eso de arriba para darle nombre al admin
    def __str__(self):
        """Unicode representation of Persona."""
        return f'{self.nombre} - {self.edad} - {self.oficina}'