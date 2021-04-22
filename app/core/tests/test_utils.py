from unittest import TestCase
from core.utils import normalize_email_domain_name


class TestUtils(TestCase):
    def test_normalize_email_domain_name(self):
        """should return email with normalized domain name"""
        email = 'username@DoMainE.CoM'
        normalized_email = normalize_email_domain_name(email)
        expected_email = 'username@domaine.com'

        self.assertEqual(normalized_email, expected_email)
