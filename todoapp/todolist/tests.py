from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class IndexTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username='bob', password='pass')
        cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.login(**self.credentials)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Обязательно к исполнению')
