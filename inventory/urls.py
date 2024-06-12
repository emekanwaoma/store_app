from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r"suppliers", SupplierViewSet)
router.register(r"items", ItemViewSet)

urlpatterns = [
    path("inventory/", include(router.urls)),
]
