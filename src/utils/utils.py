from bson import Decimal128


def convert_decimal_128(v):
    return Decimal128(str(v))
