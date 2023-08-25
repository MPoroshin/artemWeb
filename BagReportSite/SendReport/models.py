from django.db import models

# Create your models here.
class BagReport(models.Model):
    text = models.CharField(max_length=200)
    name_user =  models.CharField(max_length=100)
    date_added = models.DateTimeField(
        auto_now_add=True)
    phone = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
