from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from zope import schema
from zope.interface import implementer


class ICampus(Schema):
    """Scheme of campus"""

    title = schema.TextLine(title=_("campus_title", default="Campus"), required=True)

    description = schema.Text(title=_("campus_city", default="City"), required=True)

    # director = RelationChoice(
    #     title=_("director_person", default="Director"),
    #     vocabulary="portal_uft.vocabulary.person",
    #     required=True,
    # )


@implementer
class Campus(Container):
    """Class type campus"""
