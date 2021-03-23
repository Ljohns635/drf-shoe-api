from django.conf.urls import include, url
from rest_framework import routers

from api.views import ManufacturerViewSet, ShoeViewSet, ShoeColorViewSet, ShoeTypeViewSet

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'shoe', ShoeViewSet)
router.register(r'color', ShoeColorViewSet)
router.register(r'type', ShoeTypeViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
]

