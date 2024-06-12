from rest_framework import serializers

from .models import Item, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    suppliers = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all())

    class Meta:
        model = Item
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        suppliers_data = []
        for supplier in instance.suppliers.all():
            supplier_serializer = SupplierSerializer(supplier)
            supplier_data = supplier_serializer.data
            suppliers_data.append(supplier_data)
        representation["suppliers"] = suppliers_data
        return representation
