from kitconcept import api
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from portal_uft.content.person import Person
from typing import List
from zope import schema
from zope.interface import implementer


class ICampus(Schema):
    """Scheme of campus"""

    city = schema.Choice(
        title=_("city", default="City"),
        vocabulary="portal_uft.vocabulary.cities",
        default="",
        required=True,
    )

    title = schema.TextLine(
        title=_("campus_nome", default="Campus"),
        required=True,
    )
    description = schema.Text(title=_("campus_description"), required=False)

    # director = RelationChoice(
    #     title=_("director_person", default="Director"),
    #     vocabulary="portal_uft.vocabulary.person",
    #     required=True,
    # )


@implementer(ICampus)
class Campus(Container):
    """Class type campus"""

    def persons(self) -> List[Person]:
        """Return a list of persons connected to this Campus."""
        persons = [
            rel.from_object
            for rel in api.relation.get(target=self, relationship="campus")
        ]
        return persons
