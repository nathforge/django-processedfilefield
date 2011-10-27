from django.core.files.base import File, ContentFile
from django.db import models


def create_field(name, file_field_bases, field_file_bases):
    class FieldFile(ProcessedFieldFileMixin, field_file_bases):
        pass
    
    class FileField(ProcessedFileFieldMixin, file_field_bases):
        attr_class = FieldFile
    
    FileField.__name__ = name
    return FileField


class ProcessedFieldFileMixin(object):
    def save(self, name, content, save=True):
        super(ProcessedFieldFileMixin, self).save(name, content, save)
        for variation_name, transform in self.field.variations.iteritems():
            try:
                self.instance._meta.get_field_by_name(variation_name)
            except models.FieldDoesNotExist:
                raise NameError('Variation "%s" must also be the name of a field on %s' % (
                    variation_name, type(self.instance).__name__,)
                )
            
            content.seek(0)
            transformed_file = transform(content)
            
            if not isinstance(transformed_file, File):
                if not isinstance(transformed_file, str):
                    raise ValueError('Variation "%s" didn\'t return a File object or a string' % (
                        variation_name,
                    ))
                else:
                    transformed_file = ContentFile(transformed_file)
            
            transformed_file.name = name
            setattr(self.instance, variation_name, transformed_file)


class ProcessedFileFieldMixin(object):
    def __init__(self, *args, **kwargs):
        self.variations = kwargs.pop('variations')
        super(ProcessedFileFieldMixin, self).__init__(*args, **kwargs)
