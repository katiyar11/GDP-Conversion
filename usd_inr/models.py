from django.db import models
import uuid


class GdpData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True, blank=True)
    usd_data = models.DecimalField(null=True, blank=True, default=None, decimal_places=2, max_digits=16)

