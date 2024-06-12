from django.contrib import admin
from django.db import models
from django.utils import timezone


class _BaseModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(archived__isnull=True).filter(archived=None)


class BaseModelQuerySet(models.QuerySet):
    pass


BaseModelManager = _BaseModel.from_queryset(BaseModelQuerySet)


class BaseModel(models.Model):
    archived = models.DateTimeField(blank=True, null=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = BaseModelManager()
    super_objects = models.Manager()

    def archive(self, using=None, keep_parents=False):
        self.archived = timezone.now()
        super().save(using=using)

    class Meta:
        abstract = True
        ordering = ["-last_updated"]

    def lock(self) -> None:
        type(self).objects.filter(pk=self.pk).select_for_update().values_list("pk")

    def __hash__(self):
        return super().__hash__()


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ["date_created", "last_modified"]
