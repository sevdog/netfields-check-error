from django.db import InternalError, connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from .models import AssignableIP


class ModelTestCase(TestCase):

    def test_creating_and_save(self):
        instance = AssignableIP.objects.create(current_ip="192.168.0.1", network="192.168.0.0/24")
        instance = AssignableIP.objects.get(pk=instance.pk)
        with (
            self.assertLogs('django.db.models') as logger,
            CaptureQueriesContext(connection) as ctx
        ):
            instance.full_clean()
        with self.assertRaisesMessage(InternalError, 'current transaction is aborted, commands ignored until end of transaction block'):
            instance.save()
        print(ctx.captured_queries, logger.output)

    def test_creating_and_save_with_none(self):
        instance = AssignableIP.objects.create(current_ip=None, network="192.168.0.0/24")
        instance = AssignableIP.objects.get(pk=instance.pk)
        with (
            CaptureQueriesContext(connection) as ctx
        ):
            instance.full_clean()
        instance.save()
        print(ctx.captured_queries)

    def test_instantiating(self):
        instance = AssignableIP(current_ip="192.168.0.1", network="192.168.0.0/24")
        with (
            self.assertLogs('django.db.models') as logger,
            CaptureQueriesContext(connection) as ctx
        ):
            instance.full_clean()
        with self.assertRaisesMessage(InternalError, 'current transaction is aborted, commands ignored until end of transaction block'):
            instance.save()
        print(ctx.captured_queries, logger.output)

    def test_instantiating_with_none(self):
        instance = AssignableIP(current_ip=None, network="192.168.0.0/24")
        with (
            CaptureQueriesContext(connection) as ctx
        ):
            instance.full_clean()
        instance.save()
        print(ctx.captured_queries)
