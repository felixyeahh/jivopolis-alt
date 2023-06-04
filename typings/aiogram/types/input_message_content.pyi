"""
This type stub file was generated by pyright.
"""

import typing
from . import base
from .message_entity import MessageEntity
from .labeled_price import LabeledPrice

class InputMessageContent(base.TelegramObject):
    """
    This object represents the content of a message to be sent as a result of an inline query.

    Telegram clients currently support the following 4 types

    https://core.telegram.org/bots/api#inputmessagecontent
    """
    ...


class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    phone_number: base.String = ...
    first_name: base.String = ...
    last_name: typing.Optional[base.String] = ...
    vcard: typing.Optional[base.String] = ...
    def __init__(self, phone_number: base.String, first_name: base.String = ..., last_name: typing.Optional[base.String] = ..., vcard: typing.Optional[base.String] = ...) -> None:
        ...
    


class InputInvoiceMessageContent(InputMessageContent):
    """
    Represents the content of an invoice message to be sent as the
    result of an inline query.

    https://core.telegram.org/bots/api#inputinvoicemessagecontent
    """
    title: base.String = ...
    description: base.String = ...
    payload: base.String = ...
    provider_token: base.String = ...
    currency: base.String = ...
    prices: typing.List[LabeledPrice] = ...
    max_tip_amount: typing.Optional[base.Integer] = ...
    suggested_tip_amounts: typing.Optional[typing.List[base.Integer]] = ...
    provider_data: typing.Optional[base.String] = ...
    photo_url: typing.Optional[base.String] = ...
    photo_size: typing.Optional[base.Integer] = ...
    photo_width: typing.Optional[base.Integer] = ...
    photo_height: typing.Optional[base.Integer] = ...
    need_name: typing.Optional[base.Boolean] = ...
    need_phone_number: typing.Optional[base.Boolean] = ...
    need_email: typing.Optional[base.Boolean] = ...
    need_shipping_address: typing.Optional[base.Boolean] = ...
    send_phone_number_to_provider: typing.Optional[base.Boolean] = ...
    send_email_to_provider: typing.Optional[base.Boolean] = ...
    is_flexible: typing.Optional[base.Boolean] = ...
    def __init__(self, title: base.String, description: base.String, payload: base.String, provider_token: base.String, currency: base.String, prices: typing.List[LabeledPrice] = ..., max_tip_amount: typing.Optional[base.Integer] = ..., suggested_tip_amounts: typing.Optional[typing.List[base.Integer]] = ..., provider_data: typing.Optional[base.String] = ..., photo_url: typing.Optional[base.String] = ..., photo_size: typing.Optional[base.Integer] = ..., photo_width: typing.Optional[base.Integer] = ..., photo_height: typing.Optional[base.Integer] = ..., need_name: typing.Optional[base.Boolean] = ..., need_phone_number: typing.Optional[base.Boolean] = ..., need_email: typing.Optional[base.Boolean] = ..., need_shipping_address: typing.Optional[base.Boolean] = ..., send_phone_number_to_provider: typing.Optional[base.Boolean] = ..., send_email_to_provider: typing.Optional[base.Boolean] = ..., is_flexible: typing.Optional[base.Boolean] = ...) -> None:
        ...
    


class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    latitude: base.Float = ...
    longitude: base.Float = ...
    horizontal_accuracy: typing.Optional[base.Float] = ...
    live_period: typing.Optional[base.Integer] = ...
    heading: typing.Optional[base.Integer] = ...
    proximity_alert_radius: typing.Optional[base.Integer] = ...
    def __init__(self, latitude: base.Float, longitude: base.Float, horizontal_accuracy: typing.Optional[base.Float] = ..., live_period: typing.Optional[base.Integer] = ..., heading: typing.Optional[base.Integer] = ..., proximity_alert_radius: typing.Optional[base.Integer] = ...) -> None:
        ...
    


class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    message_text: base.String = ...
    parse_mode: typing.Optional[base.String] = ...
    entities: typing.Optional[typing.List[MessageEntity]] = ...
    disable_web_page_preview: base.Boolean = ...
    def safe_get_parse_mode(self): # -> Any | None:
        ...
    
    def safe_get_disable_web_page_preview(self): # -> Any | None:
        ...
    
    def __init__(self, message_text: base.String, parse_mode: typing.Optional[base.String] = ..., entities: typing.Optional[typing.List[MessageEntity]] = ..., disable_web_page_preview: typing.Optional[base.Boolean] = ...) -> None:
        ...
    


class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    latitude: base.Float = ...
    longitude: base.Float = ...
    title: base.String = ...
    address: base.String = ...
    foursquare_id: typing.Optional[base.String] = ...
    foursquare_type: typing.Optional[base.String] = ...
    google_place_id: typing.Optional[base.String] = ...
    google_place_type: typing.Optional[base.String] = ...
    def __init__(self, latitude: base.Float, longitude: base.Float, title: base.String, address: base.String, foursquare_id: typing.Optional[base.String] = ..., foursquare_type: typing.Optional[base.String] = ..., google_place_id: typing.Optional[base.String] = ..., google_place_type: typing.Optional[base.String] = ...) -> None:
        ...
    

