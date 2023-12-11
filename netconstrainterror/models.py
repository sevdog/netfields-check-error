from django.db import models
from netfields import CidrAddressField, InetAddressField


class AssignableIP(models.Model):
    current_ip = InetAddressField(default=None, null=True, blank=True)
    network = CidrAddressField()

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(network__net_contains=models.F('current_ip')) | models.Q(current_ip__isnull=True) ,
                name='ip_in_range'
            ),
        )
