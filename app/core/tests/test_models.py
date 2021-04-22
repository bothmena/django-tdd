from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user(self):
        """test creating a new user with an email is successful"""
        email = 'test@bothmena.me'
        password = 'testPASS'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_normalized_email(self):
        """should normalize domain name in email address"""
        email = 'test@BoThMeNa.Me'
        password = 'testPass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        expected_email = 'test@bothmena.me'
        self.assertEqual(user.email, expected_email)

    def test_create_user_validation_email_none(self):
        """should raise ValueError if email is None"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """should create super user"""
        user = get_user_model().objects.create_superuser('email@blabla.com', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
