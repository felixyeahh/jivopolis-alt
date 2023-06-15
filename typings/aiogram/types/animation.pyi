"""
This type stub file was generated by pyright.
"""
# flake8: noqa
from . import base, mixins
from .photo_size import PhotoSize


class Animation(base.TelegramObject, mixins.Downloadable):
    """
    You can provide an animation for your game so that it looks stylish in chats
    (check out Lumberjack for an example).
    This object represents an animation file to be displayed in the message containing a game.

    https://core.telegram.org/bots/api#animation
    """
    file_id: base.String = ...
    file_unique_id: base.String = ...
    width: base.Integer = ...
    height: base.Integer = ...
    duration: base.Integer = ...
    thumb: PhotoSize = ...
    file_name: base.String = ...
    mime_type: base.String = ...
    file_size: base.Integer = ...
