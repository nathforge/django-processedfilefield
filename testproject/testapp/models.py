import os
import sys

sys.path = [
    os.path.join(os.path.dirname(__file__), '../../src'),
] + sys.path

from django.db import models
from processedfilefield import ProcessedFileField


class TestModel(models.Model):
    content = ProcessedFileField(upload_to='content', variations=dict(
        content_first_10_bytes=lambda file: file.read()[:10]
    ))
    content_first_10_bytes = models.FileField(upload_to='content_first_10_bytes')
