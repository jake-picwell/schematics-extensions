import copy

from schematics.models import Model, ModelDict


def __deepcopy__(self, memo):
    """
    This is here temporarily to resolve an issue with schematics models not
    being able to be deepcopied/pickled.

    Open issue here: https://github.com/schematics/schematics/issues/510
    """
    copied = ModelDict(
        *map(lambda o: copy.deepcopy(o, memo), [
            self._unsafe, self._converted, self._ModelDict__valid])
    )
    return copied

ModelDict.__deepcopy__ = __deepcopy__


class Model(Model):

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls.get_mock_object(overrides=kwargs)

    @classmethod
    def get_null_object(cls, overrides=None):
        if overrides is None:
            overrides = {}
        values = {}
        for name, field in cls.fields.items():
            if name not in overrides:
                values[name] = field.null()
        values.update(overrides)
        return cls(values)

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self._data)

    def __hash__(self):
        return id(self)
