"""
This type stub file was generated by pyright.
"""

import typing
from . import base
from .animation import Animation
from .message_entity import MessageEntity
from .photo_size import PhotoSize


class Game(base.TelegramObject):
    """
    This object represents a game.

    Use BotFather to create and edit games, their short names will act as\
         unique identifiers.

    https://core.telegram.org/bots/api#game
    """
    title: base.String = ...
    description: base.String = ...
    photo: typing.List[PhotoSize] = ...
    text: base.String = ...
    text_entities: typing.List[MessageEntity] = ...
    animation: Animation = ...
