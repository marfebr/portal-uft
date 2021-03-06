from kitconcept import api
from portal_uft.content.campus import Campus
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _update_tags(obj: Campus):
    """Update tags on Campus object."""
    vocab = api.vocabulary.get("portal_uft.vocabulary.cities")
    # tags = set(obj.subject)
    tags = {tag for tag in obj.subject if not tag.startswith("Campus: ")}
    city = obj.city
    term = vocab.getTermByToken(city)
    tags.add(f"Campus: {term.title}")
    obj.subject = tuple(tags)


def added(obj: Campus, event: ObjectAddedEvent):
    """Post creation handler for Campus."""
    # Verificar se grupo existe
    group = api.group.get(groupname=obj.title)
    # criar caso não exista
    if not group:
        api.group.create(
            groupname=obj.title,
        )
    _update_tags(obj)


def modified(obj: Campus, event: ObjectModifiedEvent):
    """Post modification handler for Campus."""
    _update_tags(obj)
