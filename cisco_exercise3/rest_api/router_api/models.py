from django.db import models


# Create your models here.
class RouterDetails(models.Model):

    class Meta:
        db_table = 'router_details'
        unique_together = (('loopback', 'hostname'),)

    sapid = models.CharField(max_length=256)
    hostname = models.CharField(max_length=256)
    loopback = models.GenericIPAddressField()
    mac_addr = models.CharField(max_length=256)
    active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sapid
