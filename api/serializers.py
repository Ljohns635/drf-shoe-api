from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from shoeapp.models import Manufacturer, ShoeColor, ShoeType, Shoe

class ManufacturerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Manufacturer
        fields = (
            "id",
            "name",
            "website"
        )

class ShoeColorSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ShoeColor
        fields = (
            "id",
            "color_name",
        )

class ShoeTypeSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ShoeType
        fields = (
            "id",
            "style",
        )

class ShoeSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Shoe
        fields = (
            "id",
            "size",
            "brand_name",
            "manufacturer",
            "color",
            "material",
            "shoe_type",
            "fasten_type",
        )