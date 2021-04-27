from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Inventory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    edition = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    covertype = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


    def _str_(self):
        return self.title