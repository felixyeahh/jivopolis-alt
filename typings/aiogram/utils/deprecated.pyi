"""
This type stub file was generated by pyright.
"""

from typing import Callable, Generic, Optional, Type, TypeVar

def deprecated(reason, stacklevel=...) -> Callable:
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.

    Source: https://stackoverflow.com/questions/2536307/decorators-in-the-python-standard-lib-deprecated-specifically
    """
    ...

def warn_deprecated(message, warning=..., stacklevel=...): # -> None:
    ...

def renamed_argument(old_name: str, new_name: str, until_version: str, stacklevel: int = ...): # -> (func: Unknown) -> ((*args: Unknown, **kwargs: Unknown) -> Coroutine[Any, Any, Unknown]):
    """
    A meta-decorator to mark an argument as deprecated.

    .. code-block:: python3

        @renamed_argument("chat", "chat_id", "3.0")  # stacklevel=3 by default
        @renamed_argument("user", "user_id", "3.0", stacklevel=4)
        def some_function(user_id, chat_id=None):
            print(f"user_id={user_id}, chat_id={chat_id}")

        some_function(user=123)  #  prints 'user_id=123, chat_id=None' with warning
        some_function(123)  #  prints 'user_id=123, chat_id=None' without warning
        some_function(user_id=123)  #  prints 'user_id=123, chat_id=None' without warning


    :param old_name:
    :param new_name:
    :param until_version: the version in which the argument is scheduled to be removed
    :param stacklevel: leave it to default if it's the first decorator used.
    Increment with any new decorator used.
    :return: decorator
    """
    ...

def removed_argument(name: str, until_version: str, stacklevel: int = ...): # -> (func: Unknown) -> ((*args: Unknown, **kwargs: Unknown) -> Coroutine[Any, Any, Unknown]):
    """
    A meta-decorator to mark an argument as removed.

    .. code-block:: python3

        @removed_argument("until_date", "3.0")  # stacklevel=3 by default
        def some_function(user_id, chat_id=None):
            print(f"user_id={user_id}, chat_id={chat_id}")

    :param name:
    :param until_version: the version in which the argument is scheduled to be removed
    :param stacklevel: leave it to default if it's the first decorator used.
    Increment with any new decorator used.
    :return: decorator
    """
    ...

_VT = TypeVar("_VT")
_OwnerCls = TypeVar("_OwnerCls")
class DeprecatedReadOnlyClassVar(Generic[_OwnerCls, _VT]):
    """
    DeprecatedReadOnlyClassVar[Owner, ValueType]

    :param warning_message: Warning message when getter gets called
    :param new_value_getter: Any callable with (owner_class: Type[Owner]) -> ValueType
                             signature that will be executed

    Usage example:

    >>> class MyClass:
    ...     some_attribute: DeprecatedReadOnlyClassVar[MyClass, int] = \
    ...            DeprecatedReadOnlyClassVar(
    ...                  "Warning message.", lambda owner: 15)
    ...
    >>> MyClass.some_attribute  # does warning.warn with `Warning message` and returns 15 in the current case
    """
    __slots__ = ...
    def __init__(self, warning_message: str, new_value_getter: Callable[[_OwnerCls], _VT]) -> None:
        ...
    
    def __get__(self, instance: Optional[_OwnerCls], owner: Type[_OwnerCls]): # -> _VT@DeprecatedReadOnlyClassVar:
        ...
    


