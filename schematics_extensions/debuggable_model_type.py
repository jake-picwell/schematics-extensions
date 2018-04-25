from schematics.types import BaseType
from schematics.transforms import blacklist

from . import MockableDictType as DictType
from .models import Model


class DebuggableModel(Model):
    """Model that has a 'debug' field and a 'debug' role which allows it to be
    displayed.
    """

    debug = DictType(BaseType, default={})

    class Options:
        roles = {
            'default': blacklist('debug'),
            'debug': blacklist()
        }

    def to_primitive(self, *args, **kwargs):
        """ Don't require submodels to have parent's 'debug' role."""
        return super(DebuggableModel, self).to_primitive(
            raise_error_on_role=False, *args, **kwargs)
