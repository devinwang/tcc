from django.shortcuts import reverse
from django.test import TestCase
from django.test.client import Client


# Create your tests here.
class TestMainView(TestCase):
    def test_main(self):
        client = Client()
        rsp = client.get(reverse('index'))
        self.assertEqual(rsp.status_code, 404)
