from django.db import models


class DatasetUploadModel(models.Model):
    dataset = models.FileField()
    date_uploaded = models.DateTimeField(auto_now=True)
