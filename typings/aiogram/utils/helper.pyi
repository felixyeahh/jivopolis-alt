"""
This type stub file was generated by pyright.
"""

from typing import List

"""
Example:
    >>> from aiogram.utils.helper import Helper, ListItem, HelperMode, Item
    >>> class MyHelper(Helper):
    ...     mode = HelperMode.lowerCamelCase
    ...     FOO_ITEM = ListItem()
    ...     BAR_ITEM = ListItem()
    ...     BAZ_ITEM = ListItem()
    ...     LOREM = Item()
    ...
    >>> print(MyHelper.FOO_ITEM & MyHelper.BAR_ITEM)
    <<<  ['fooItem', 'barItem']
    >>> print(MyHelper.all())
    <<<  ['barItem', 'bazItem', 'fooItem', 'lorem']
"""
PROPS_KEYS_ATTR_NAME = ...
class Helper:
    mode = ...
    @classmethod
    def all(cls): # -> list[Unknown]:
        """
        Get all consts
        :return: list
        """
        ...
    


class HelperMode(Helper):
    mode = ...
    SCREAMING_SNAKE_CASE = ...
    lowerCamelCase = ...
    CamelCase = ...
    snake_case = ...
    lowercase = ...
    @classmethod
    def all(cls): # -> list[str]:
        ...
    
    @classmethod
    def apply(cls, text, mode): # -> LiteralString | str:
        """
        Apply mode for text

        :param text:
        :param mode:
        :return:
        """
        ...
    


class Item:
    """
    Helper item

    If a value is not provided,
    it will be automatically generated based on a variable's name
    """
    def __init__(self, value=...) -> None:
        ...
    
    def __get__(self, instance, owner): # -> str | None:
        ...
    
    def __set_name__(self, owner, name): # -> None:
        ...
    


class ListItem(Item):
    """
    This item is always a list

    You can use &, | and + operators for that.
    """
    def add(self, other):
        ...
    
    def __get__(self, instance, owner): # -> ItemsList:
        ...
    
    def __getitem__(self, item): # -> str | None:
        ...
    
    __iadd__ = ...


class ItemsList(list):
    """
    Patch for default list

    This class provides +, &, |, +=, &=, |= operators for extending the list
    """
    def __init__(self, *seq) -> None:
        ...
    
    def add(self, other): # -> Self@ItemsList:
        ...
    
    __iadd__ = ...


class OrderedHelperMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs): # -> Self@OrderedHelperMeta:
        ...
    


class OrderedHelper(metaclass=OrderedHelperMeta):
    mode = ...
    @classmethod
    def all(cls) -> List[str]:
        """
        Get all Items values
        """
        ...
    


