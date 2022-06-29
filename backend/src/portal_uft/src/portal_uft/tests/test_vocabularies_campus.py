from kitconcept import api

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


VOCABULARY = "portal_uft.vocabulary.campus"


class TestIndustriesVocabulary(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING
    portal_type = "campus"

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        obj = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Palmas",
            description="Campus da UFT em Palmas",
            city="palmas",
            email="palmas@uft.edu.br",
            extension="2022",
        )
        obj1 = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Miracema",
            description="Campus da UFT em Miracema",
            city="miracema",
            email="miracema@uft.edu.br",
            extension="5555",
        )

    def test_vocabulary(self):
        vocab = api.vocabulary.get(VOCABULARY)

        items = [item for item in vocab]

        self.assertEqual(len(items), 2)

    def test_vocabulary_titles(self):
        vocab = api.vocabulary.get(VOCABULARY)

        items = [item.title for item in vocab]

        self.assertIn("Palmas", items)
        self.assertIn("Miracema", items)
