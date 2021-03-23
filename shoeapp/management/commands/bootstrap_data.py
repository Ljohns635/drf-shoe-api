from django.core.management.base import BaseCommand
from shoeapp.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Adds type of Shoe and Color for Database'
    def add_arguments(self, parser):
        parser.add_argument('style', choices=['sneaker', 'boot', 'sandal', 'dress', 'other'], type=str, nargs=5, help='Options: sneaker, boot, sandal, dress, other')
        parser.add_argument('color_name', choices=['red','orange','yellow','green','blue','indigo','violet','white','black'], type=str, nargs=9, help='Options: red, orange, yellow, green, blue, indigo, violet, white, black')
    
    def handle(self, *args, **options):
        # recieved help from my facilitator Elizabeth Scheidt
        for (var, item) in ShoeType.TYPES:
            ShoeType.objects.create(style=var)
        for (color, item) in ShoeColor.CHOICES:
            ShoeColor.objects.create(color_name=color)

        self.stdout.write(self.style.SUCCESS('Added Bootstrap Data!'))