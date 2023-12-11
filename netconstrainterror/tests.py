from django.test import TestCase
from .models import AssignableIP


class ModelTestCase(TestCase):

    def test_with_null_ip(self):
        instance = AssignableIP(current_ip=None, network="192.168.0.0/24")
        instance.full_clean()

    def test_with_not_null_ip(self):
        instance = AssignableIP(current_ip="192.168.0.1", network="192.168.0.0/24")
        instance.full_clean()