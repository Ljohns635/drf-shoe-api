from django.core.management.base import BaseCommand
from shoeapp.models import ShoeType

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('style')
    
    def handle(self, *args, **options):
        shoetype = ShoeType(
            style = options['style'],
        )
        shoetype.save()
        self.stdout.write(self.style.SUCCESS('Added style!'))