from ipaddress import ip_address, ip_network
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from .models import AssignableIP


class ModelTestCase(TestCase):

    def test_with_null_ip(self):
        instance = AssignableIP(current_ip=None, network="192.168.0.0/24")
        with CaptureQueriesContext(connection) as ctx:
            instance.full_clean()
        print('Null and string', ctx.captured_queries)

    def test_with_not_null_ip(self):
        instance = AssignableIP(current_ip="192.168.0.1", network="192.168.0.0/24")
        with CaptureQueriesContext(connection) as ctx:
            instance.full_clean()
        print('string and string', ctx.captured_queries)

    def test_with_not_null_ip_bis(self):
        instance = AssignableIP(current_ip=ip_address("192.168.0.1"), network=ip_network("192.168.0.0/24"))
        with CaptureQueriesContext(connection) as ctx:
            instance.full_clean()
        print('ipaddres and ipnetwork', ctx.captured_queries)

    def test_with_null_ip_bis(self):
        instance = AssignableIP(current_ip=None, network=ip_network("192.168.0.0/24"))
        with CaptureQueriesContext(connection) as ctx:
            instance.full_clean()
        print('null and ipnetwork', ctx.captured_queries)