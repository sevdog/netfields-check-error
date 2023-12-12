from django.test import TestCase
from .models import AssignableIP


class ModelTestCase(TestCase):

    def test_with_loading_from_db(self):
        instance = AssignableIP.objects.create(current_ip="192.168.0.1", network="192.168.0.0/24")

        instance = AssignableIP.objects.select_for_update().get(pk=instance.pk)
        with self.assertLogs('django.db.models') as logger:
            instance.full_clean()
        try:
            instance.save()
        except:
            pass
        print(logger.output)
