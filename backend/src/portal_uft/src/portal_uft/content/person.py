"""person profile in the site"""
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel.model import Schema
from portal_uft import _
from zope import schema
from zope.interface import implementer


class IPerson(Schema):
    """Schema of person profile"""

    title = schema.TextLine(title=_("person_title", default="Fullname"), required=True)
    description = schema.Text(
        title=_("perso_description", default="Biography"), required=False
    )

    email = Email(title=_("person_email", default="Email"), required=True)
    extension = schema.TextLine(title=_("Extension"), required=False)


@implementer(IPerson)
class Person(Container):
    """Class type profile"""
