from django.contrib import admin
from shoeapp.models import Shoe, ShoeColor, ShoeType, Manufacturer
# Register your models here.
admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Manufacturer)