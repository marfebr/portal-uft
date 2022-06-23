from plone.dexterity.content import Container

# from plone.schema.email import Email
from plone.supermodel.model import Schema
from portal_uft import _
from portal_uft import validators
from z3c.relationfield import RelationChoice
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class ICampus(Schema):
    """Scheme of campus"""

    title = schema.TextLine(title=_("campus_title", default="Campus"), required=True)

    description = schema.Text(title=_("campus_city", default="City"), required=True)

    director = RelationChoice(
        title=_("director_person", default="Director"),
        vocabulary="portal_uft.content.person",
        required=True,
    )


@implementer
class Campus(Container):
    """Class type campus"""
