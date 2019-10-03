from django.db import models


class PartsDemand(models.Model):
    description = models.CharField(max_length=500, blank=True, default='')
    delivery_addr = models.CharField(max_length=200, blank=True, default='')
    contact_info = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='parts_demand', on_delete=models.CASCADE)
    conclusion_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(PartsDemand, self).save(*args, **kwargs)

    class Meta:
        ordering = ['conclusion_status']