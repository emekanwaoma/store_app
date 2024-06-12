from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ItemViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
