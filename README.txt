django-processedfilefield: Post-processing for Django FileFields. Takes a dict
of field names on the model, mapped to post-processing functions. These
functions could convert a PDF to text, thumbnail an image, etc.

Example:
    >>> class TestModel(models.Model):
    ...     content = ProcessedFileField(upload_to='content', variations=dict(
    ...         content_first_10_bytes=lambda file: file.read()[:10]
    ...     ))
    ...     content_first_10_bytes = models.FileField(upload_to='content_first_10_bytes')
    ... 
    >>> obj = TestModel.objects.create()
    >>> obj.content = ContentFile('abcdefghijklmnopqrstuvwxyz')
    >>> obj.content.name = 'alphabet'
    >>> obj.save()
    >>> 
    >>> assert obj.content_first_10_bytes.read() == 'abcdefghij'
