"""
This type stub file was generated by pyright.
"""

from . import base

class ResponseParameters(base.TelegramObject):
    """
    Contains information about why a request was unsuccessful.

    https://core.telegram.org/bots/api#responseparameters
    """
    migrate_to_chat_id: base.Integer = ...
    retry_after: base.Integer = ...

