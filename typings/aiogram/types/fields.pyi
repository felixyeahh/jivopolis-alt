"""
This type stub file was generated by pyright.
"""

# flake8: noqa
import abc
import datetime
import sys
from typing import Any

__all__ = (
    'BaseField', 'Field', 'ListField', 'DateTimeField', 'TextField',
    'ListOfLists', 'ConstField'
)


class BaseField(metaclass=abc.ABCMeta):
    """
    Base field (prop)
    """
    def __init__(self, *, base=..., default=..., alias=..., on_change=...) -> None: # noqa
        """
        Init prop

        :param base: class for child element
        :param default: default value
        :param alias: alias name (for e.g. field 'from' has to be named \
            'from_user' as 'from' is a builtin Python keyword
        :param on_change: callback will be called when value is changed
        """
        ...

    def __set_name__(self, owner, name) -> None:
        ...

    def resolve_base(self, instance) -> None:
        ...

    def get_value(self, instance) -> Any:
        """
        Get value for the current object instance

        :param instance:
        :return:
        """
        ...

    def set_value(self, instance, value, parent=...) -> None:
        """
        Set prop value

        :param instance:
        :param value:
        :param parent:
        :return:
        """
        ...

    def __get__(self, instance, owner):
        ...

    def __set__(self, instance, value) -> None:
        ...

    @abc.abstractmethod
    def serialize(self, value) -> None:
        """
        Serialize value to python

        :param value:
        :return:
        """
        ...

    @abc.abstractmethod
    def deserialize(self, value, parent=...) -> None:
        """Deserialize python object value to TelegramObject value"""
        ...

    def export(self, instance) -> None:
        """
        Alias for `serialize` but for current Object instance

        :param instance:
        :return:
        """
        ...


class Field(BaseField):
    """
    Simple field
    """
    def serialize(self, value):
        ...

    def deserialize(self, value, parent=...) -> dict[Any, Any]:
        ...


class ListField(Field):
    """
    The field contains a list of objects
    """
    def __init__(self, *args, **kwargs) -> None:
        ...

    def serialize(self, value) -> list[Any] | None:
        ...

    def deserialize(self, value, parent=...) -> list[Any | dict[Any, Any]] | None:
        ...


class ListOfLists(Field):
    def serialize(self, value) -> list[Any]:
        ...
    
    def deserialize(self, value, parent=...) -> list[Any]:
        ...
    


class DateTimeField(Field):
    """
    In this field stored datetime

    in: unixtime
    out: datetime
    """
    if sys.platform == "win32":
        ...
    else:
        def serialize(self, value: datetime.datetime) -> int:
            ...
        
    def deserialize(self, value, parent=...) -> datetime.datetime:
        ...
    


class TextField(Field):
    def __init__(self, *, prefix=..., suffix=..., default=..., alias=...) -> None:
        ...
    
    def serialize(self, value):
        ...
    
    def deserialize(self, value, parent=...) -> str:
        ...
    


class ConstField(Field):
    def __init__(self, default=..., **kwargs) -> None:
        ...
    
    def __set__(self, instance, value):
        ...
    


