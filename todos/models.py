from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Nome do Pet", max_length=100, null=False, blank=False)
    breed = models.CharField(verbose_name="Raça do Pet", max_length=100, null=True, blank=False)
    tipe = models.CharField(verbose_name="Tipo de Pet", max_length=100, null=True, blank=False)
    color = models.CharField(verbose_name="Cor do Pet", max_length=100, null=True, blank=False)
    genero = models.CharField(verbose_name="Genero", max_length=100, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Retirada", null=False, blank=False)
    finished_at = models.DateField(null=True)
    class Meta:
        ordering = ["deadline"]
    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
