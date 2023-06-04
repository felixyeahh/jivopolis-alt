"""
This type stub file was generated by pyright.
"""

import typing
from . import base

class Location(base.TelegramObject):
    """
    This object represents a point on the map.

    https://core.telegram.org/bots/api#location
    """
    longitude: base.Float = ...
    latitude: base.Float = ...
    horizontal_accuracy: typing.Optional[base.Float] = ...
    live_period: typing.Optional[base.Integer] = ...
    heading: typing.Optional[base.Integer] = ...
    proximity_alert_radius: typing.Optional[base.Integer] = ...

