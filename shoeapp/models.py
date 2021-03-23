from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    

class ShoeType(models.Model):
    SNEAKER = 'sneaker'
    BOOT = 'boot'
    SANDAL = 'sandal'
    DRESS = 'dress'
    OTHER = 'other'
    TYPES = [
        (SNEAKER, 'sneaker'),
        (BOOT, 'boot'),
        (SANDAL, 'sandal'),
        (DRESS, 'dress'),
        (OTHER, 'other'),
    ]
    style = models.CharField(
        max_length=9,
        choices=TYPES
    )

    def __str__(self):
        return self.style
    

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
        (RED, 'red'),
        (ORANGE, 'orange'),
        (YELLOW, 'yellow'),
        (GREEN, 'green'),
        (BLUE, 'blue'),
        (INDIGO, 'indigo'),
        (VIOLET, 'violet'),
        (WHITE, 'white'),
        (BLACK, 'black')
    ]
    color_name = models.CharField(
        max_length=9,
        choices=CHOICES,
    )

    def __str__(self):
        return self.color_name
    

class Shoe(models.Model):
    size = models.FloatField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    color = models.ForeignKey('ShoeColor', on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey('ShoeType', on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand_name} | {self.manufacturer}'
    