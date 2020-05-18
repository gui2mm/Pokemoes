from django.core.management.base import BaseCommand
from core_app.models import TablePokemonNames

class FetchApi(BaseCommand):
    help = "Update DB with https://pokeapi.co/"

    def add_arguments(self, parser):
        parser.add_argument('')