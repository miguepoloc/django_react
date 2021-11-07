from django.db import models


class Todo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def _str_(self):
        return self.titulo
