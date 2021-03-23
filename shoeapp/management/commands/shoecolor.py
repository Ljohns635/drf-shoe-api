from django.core.management.base import BaseCommand
from shoeapp.models import ShoeColor

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('color_name', choices=['red','orange','yellow','green','blue','indigo','violet','white','black'])
    
    def handle(self, *args, **options):
        shoecolor = ShoeColor(
            color_name = options['color_name'],
        )
        shoecolor.save()
        self.stdout.write(self.style.SUCCESS('Added Color!'))