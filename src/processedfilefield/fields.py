from django.db import models
from django.db.models.fields import files
from processedfilefield.mixins import create_field


ProcessedFileField = create_field(
    name='ProcessedFileField',
    file_field_bases=models.FileField,
    field_file_bases=files.FieldFile,
)
