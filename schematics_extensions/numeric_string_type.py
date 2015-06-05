from random import choice, randint
import re
import string

from schematics.exceptions import ValidationError
from .types import StringType


class NumericStringType(StringType):
    """String that contains only digits.

    Parameters:
        length (int): Exact number of digits the string can contains. Optional.

    Example usage:

        class MyModel(Model):
            my_field = NumericStringType(length=5)
    """

    MESSAGES = {'length': u'Value is not a numeric string of length %d'}

    REGEX_PATTERN = r'^\d{%d}$'

    def __init__(self, **kwargs):
        self.length = kwargs.pop('length', None)
        super(NumericStringType, self).__init__(**kwargs)

    def _mock(self, context=None):
        length = self.length if self.length else randint(1, self.max_length
                                                         if self.max_length
                                                         else 20)
        return ''.join(choice(string.digits) for _ in range(length))

    def validate_length(self, value):
        if self.length and len(value) == self.length:
            if not re.compile(self.REGEX_PATTERN % self.length).match(value):
                raise ValidationError(self.messages['length'] % self.length)
