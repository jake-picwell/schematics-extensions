from schematics.types import (IntType, StringType, FloatType, BooleanType,
                              NumberType, LongType)


class IntType(IntType):

    @classmethod
    def null(cls):
        return None


class CurrencyType(NumberType):
    native_type = float
    number_type = 'CurrencyType'

    def to_native(self, value, context=None):
        return round(value, 2)

    @classmethod
    def null(cls):
        return None


class StringType(StringType):

    @classmethod
    def null(cls):
        return None


class FloatType(FloatType):

    @classmethod
    def null(cls):
        return None


class BooleanType(BooleanType):

    @classmethod
    def null(cls):
        return None


class LongType(LongType):

    @classmethod
    def null(cls):
        return None
