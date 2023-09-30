import uuid

from django.db import models

class RecordedTime(models.Model):
    description = models.CharField(max_length=128, null=True, blank=True)
    project = models.CharField(max_length=64, null=True, blank=True)
    time = models.IntegerField()
    billable = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
