from enum import Enum


class ExtendedEnum(Enum):

    # @ + def convert a function to list
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OperationType(ExtendedEnum):
    CREATE = 'CREATE'
    STATUS = 'STATUS'
    EXPAND = 'EXPAND'
    DELETE = 'DELETE'


print(OperationType.list())

