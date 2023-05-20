"""
This type stub file was generated by pyright.
"""

from . import base, mixins

class PhotoSize(base.TelegramObject, mixins.Downloadable):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize
    """
    file_id: base.String = ...
    file_unique_id: base.String = ...
    width: base.Integer = ...
    height: base.Integer = ...
    file_size: base.Integer = ...


