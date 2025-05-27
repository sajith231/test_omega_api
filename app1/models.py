from django.db import models

# Create your models here.
from django.db import models

class AccAdvances(models.Model):
    slno = models.DecimalField(max_digits=12, decimal_places=0, primary_key=True)
    account = models.CharField(max_length=30, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.slno} - {self.account}"
