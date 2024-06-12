from django.contrib import admin
from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin

from inventory.models import Item, Supplier
from inventory.resources import ItemResource, SupplierResource


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"

    list_filter = [
        "content_type",
        "action_flag",
    ]

    search_fields = ["user__email", "object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "change_message",
        "content_type",
        "action_flag",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser


class ItemResourceAdmin(ImportExportModelAdmin):
    search_fields = ["name", "description", "suppliers__name"]
    resource_class = ItemResource

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


class SupplierResourceAdmin(ImportExportModelAdmin):
    search_fields = ["name", "contact"]
    resource_class = SupplierResource

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


admin.site.register(Item, ItemResourceAdmin)
admin.site.register(Supplier, SupplierResourceAdmin)
