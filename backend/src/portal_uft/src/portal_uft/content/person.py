"""person profile in the site"""
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel.model import Schema
from portal_uft import _
from portal_uft import validators
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class IPerson(Schema):
    """Schema of person profile"""

    title = schema.TextLine(title=_("person_title", default="Fullname"), required=True)
    description = schema.Text(
        title=_("perso_description", default="Biography"), required=False
    )

    # email = Email(
    #     title=_("person_email", default="Email"),
    #     required=True,
    #     # constraint=validators.is_valid_email,
    # )
    # extension = schema.TextLine(
    #     title=_("Extension"), required=False, constraint=validators.is_valid_ramal
    # )

    @invariant
    def validate_email(data):
        """Validate email"""

        value = data.email
        title = data.title
        if not (value and validators.is_valid_email(value)):
            raise validators.BadValue(
                f"The email {value} not in the uft.edu.br domain."
            )
        elif not validators.is_valid_username(title, value):
            raise validators.BadValue(
                f"The email {value} does not follow our standard."
            )


@implementer(IPerson)
class Person(Container):
    """Class type profile"""
