"""Portal settings tests."""
# plone.api
from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING  # noqa: E501

import unittest


class TestPortalSettings(unittest.TestCase):
    """Test that Portal configuration is correctly done."""

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        super().setUp()
        self.portal = self.layer["portal"]

    def test_portal_title(self):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Portal UFT Ex 8"
        self.assertEqual(value, expected)

    def test_portal_timezone(self):
        """Test portal time zone."""
        value = api.portal.get_registry_record("plone.portal_timezone")
        expected = "America/Araguaina"
        self.assertEqual(value, expected)

    def test_portal_enable_sitemap(self):
        """Test portal time zone."""
        value = api.portal.get_registry_record("plone.enable_sitemap")
        self.assertTrue(value)

    def test_portal_email_from(self):
        """Test portal time zone."""
        value = api.portal.get_registry_record("plone.email_from_address")
        expected = "uft@uft.edu.br"
        self.assertEqual(value, expected)

    def test_portal_email_host(self):
        """Test portal time zone."""
        value = api.portal.get_registry_record("plone.smtp_host")
        expected = "vinagreira.uft.edu.br"
        self.assertEqual(value, expected)

    def test_portal_email_userid(self):
        """Test portal time zone."""
        value = api.portal.get_registry_record("plone.smtp_userid")
        expected = "naoresponder@dti.uft.edu.br"
        self.assertEqual(value, expected)
