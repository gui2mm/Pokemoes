from django.core.management.base import BaseCommand
from core_app.models import TablePokemonNames
from core_app.fetchnames import namelist


class FetchApi(BaseCommand):
    help = "Update DB with https://pokeapi.co/"

    def add_model_value(self):
        table = TablePokemonNames()
        table.names = namelist()
        table.save()