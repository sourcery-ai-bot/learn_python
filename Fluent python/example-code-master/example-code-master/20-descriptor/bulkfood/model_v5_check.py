import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f'_{prefix}#{index}'
        cls.__counter += 1

    def __get__(self, instance, owner):
        return self if instance is None else getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""

INVALID = object()

class Check(Validated):

    def __init__(self, checker):
        super().__init__()
        self.checker = checker
        doc = '' if checker.__doc__ is None else f'{checker.__doc__}; '
        self.message = doc + '{!r} is not valid.'


    def validate(self, instance, value):
        result = self.checker(value)
        if result is INVALID:
            raise ValueError(self.message.format(value))
        return result
