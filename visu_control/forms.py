from django import forms
from .models import *


class DatasetUploadForm(forms.ModelForm):
    class Meta:
        model = DatasetUploadModel
        fields = ("csv_file",)
