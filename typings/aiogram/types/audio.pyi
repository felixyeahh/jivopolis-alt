"""
This type stub file was generated by pyright.
"""

from . import base, mixins
from .photo_size import PhotoSize

class Audio(base.TelegramObject, mixins.Downloadable):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio
    """
    file_id: base.String = ...
    file_unique_id: base.String = ...
    duration: base.Integer = ...
    performer: base.String = ...
    title: base.String = ...
    file_name: base.String = ...
    mime_type: base.String = ...
    file_size: base.Integer = ...
    thumb: PhotoSize = ...

