from django.db import models
from core_app.fetchnames import namelist


class TablePokemonNames(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=100)