from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import ShoeColorSerializer, ShoeSerializer, ShoeTypeSerializer, ManufacturerSerializer
from shoeapp.models import Manufacturer, Shoe, ShoeType, ShoeColor
# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()
    
class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColor.objects.all()
