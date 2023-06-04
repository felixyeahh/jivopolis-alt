"""
This type stub file was generated by pyright.
"""

from . import base

class EncryptedCredentials(base.TelegramObject):
    """
    Contains data required for decrypting and authenticating EncryptedPassportElement.
    See the Telegram Passport Documentation for a complete description of the data decryption
    and authentication processes.

    https://core.telegram.org/bots/api#encryptedcredentials
    """
    data: base.String = ...
    hash: base.String = ...
    secret: base.String = ...

