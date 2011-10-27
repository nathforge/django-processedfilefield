from django.core.files.base import ContentFile
from testproject.testapp.models import TestModel
import unittest


class TestNaturalSortField(unittest.TestCase):
    def test_processing(self):
        obj = TestModel.objects.create()
        obj.content = ContentFile('abcdefghijklmnopqrstuvwxyz')
        obj.content.name = 'alphabet'
        obj.save()
        
        self.assertEqual(obj.content_first_10_bytes.read(), 'abcdefghij')
    
    def test_empty_file(self):
        obj = TestModel.objects.create()
        
        self.assertFalse(obj.content_first_10_bytes)
