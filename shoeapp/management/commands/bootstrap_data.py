from django.core.management.base import BaseCommand
from shoeapp.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Adds type of Shoe and Color for Database'
    def add_arguments(self, parser):
        parser.add_argument('style', type=str, nargs=5, help='Options: sneaker, boot, sandal, dress, other')
        parser.add_argument('color_name', choices=['red','orange','yellow','green','blue','indigo','violet','white','black'], type=str, nargs=9, help='Options: red, orange, yellow, green, blue, indigo, violet, white, black')
    
    def handle(self, *args, **options):
        shoetype = ShoeType(
            style = options['style'],
        )
        shoecolor = ShoeColor(
            color_name = options['color_name'],
        )

        for types in options['style']:
            self.stdout.write(f'Types: {types}')
        for colors in options['color_name']:
            self.stdout.write(f'Colors: {colors}')
        shoetype.save()
        shoecolor.save()
        self.stdout.write(self.style.SUCCESS('Added Bootstrap Data!'))