from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from portal_uft import _
from portal_uft import validators
from zope import schema
from zope.interface import invariant
from zope.interface import provider


@provider(IFormFieldProvider)
class IContactInfo(model.Schema):
    """Contact information behavior."""

    model.fieldset("contact", fields=["email", "extension"])
    email = Email(title=_("person_email", default="E-mail"), required=True)

    extension = schema.TextLine(
        title=_(
            "Extension",
        ),
        required=False,
    )

    @invariant
    def validate_email(self, data):
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
