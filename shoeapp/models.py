from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

class ShoeType(models.Model):
    style = models.CharField(max_length=50)

class ShoeColor(models.Model):
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    INDIGO = 'indigo'
    VIOLET = 'violet'
    WHITE = 'white'
    BLACK = 'black'
    CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]
    color_name = models.CharField(
        max_length=9,
        choices=CHOICES,
    )

class Shoe(models.Model):
    size = models.PositiveIntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    color = models.ForeignKey('ShoeColor', on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey('ShoeType', on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)
