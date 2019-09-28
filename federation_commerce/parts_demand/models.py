from django.db import models


class PartsDemand(models.Model):
    description = models.CharField(max_length=500, blank=True, default='')
    delivery_addr = models.CharField(max_length=200, blank=True, default='')
    contact_info = models.TextField()
    announcer = models.CharField(max_length=100, blank=False, default='')
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['status']