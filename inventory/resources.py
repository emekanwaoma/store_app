from import_export import resources

from inventory.models import Item, Supplier


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item


class SupplierResource(resources.ModelResource):
    class Meta:
        model = Supplier
