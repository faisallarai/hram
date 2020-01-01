from django.test import TestCase

from accounts.models import CustomUser

class CustomUserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.setup_user('testuser', 'testpass')

    @staticmethod
    def setup_user(username, password):
        user = CustomUser.objects.create_user(username=username, password=password)
        return user

    def test_model_can_create_a_user(self):
        old_count = CustomUser.objects.count()
        self.setup_user('testuser1', 'testpass1')
        new_count = CustomUser.objects.count()
        self.assertNotEqual(old_count, new_count)

        
