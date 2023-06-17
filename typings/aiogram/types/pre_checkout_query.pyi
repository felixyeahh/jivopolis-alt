"""
This type stub file was generated by pyright.
"""

from . import base
from .order_info import OrderInfo
from .user import User


class PreCheckoutQuery(base.TelegramObject):
    """
    This object contains information about an incoming pre-checkout query.
    Your bot can offer users HTML5 games to play solo or to compete against
    each other in groups and one-on-one chats.

    Create games via @BotFather using the /newgame command.

    Please note that this kind of power requires responsibility:
    you will need to accept the terms for each game that your bots will be \
        offering.

    https://core.telegram.org/bots/api#precheckoutquery
    """
    id: base.String = ...
    from_user: User = ...
    currency: base.String = ...
    total_amount: base.Integer = ...
    invoice_payload: base.String = ...
    shipping_option_id: base.String = ...
    order_info: OrderInfo = ...

    def __hash__(self) -> int:
        ...

    def __eq__(self, other) -> bool:
        ...
