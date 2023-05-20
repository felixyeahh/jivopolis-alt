"""
This type stub file was generated by pyright.
"""

from . import base

class MessageId(base.TelegramObject):
    """
    This object represents a unique message identifier.

    https://core.telegram.org/bots/api#messageid
    """
    message_id: base.String = ...


