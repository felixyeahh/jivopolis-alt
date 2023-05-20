"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from ..utils.helper import Helper

log = ...
@dataclass(frozen=True)
class TelegramAPIServer:
    """
    Base config for API Endpoints
    """
    base: str
    file: str
    def api_url(self, token: str, method: str) -> str:
        """
        Generate URL for API methods

        :param token: Bot token
        :param method: API method name (case insensitive)
        :return: URL
        """
        ...
    
    def file_url(self, token: str, path: str) -> str:
        """
        Generate URL for downloading files

        :param token: Bot token
        :param path: file path
        :return: URL
        """
        ...
    
    @classmethod
    def from_base(cls, base: str) -> TelegramAPIServer:
        ...
    


TELEGRAM_PRODUCTION = ...
def check_token(token: str) -> bool:
    """
    Validate BOT token

    :param token:
    :return:
    """
    ...

def check_result(method_name: str, content_type: str, status_code: int, body: str): # -> Any | None:
    """
    Checks whether `result` is a valid API response.
    A result is considered invalid if:
    - The server returned an HTTP response code other than 200
    - The content of the result is invalid JSON.
    - The method call was unsuccessful (The JSON 'ok' field equals False)

    :param method_name: The name of the method called
    :param status_code: status code
    :param content_type: content type of result
    :param body: result body
    :return: The result parsed to a JSON dictionary
    :raises ApiException: if one of the above listed cases is applicable
    """
    ...

async def make_request(session, server, token, method, data=..., files=..., **kwargs): # -> Any | None:
    ...

def guess_filename(obj): # -> str | None:
    """
    Get file name from object

    :param obj:
    :return:
    """
    ...

def compose_data(params=..., files=...): # -> FormData:
    """
    Prepare request data

    :param params:
    :param files:
    :return:
    """
    ...

class Methods(Helper):
    """
    Helper for Telegram API Methods listed on https://core.telegram.org/bots/api
    """
    mode = ...
    GET_UPDATES = ...
    SET_WEBHOOK = ...
    DELETE_WEBHOOK = ...
    GET_WEBHOOK_INFO = ...
    GET_ME = ...
    LOG_OUT = ...
    CLOSE = ...
    SEND_MESSAGE = ...
    FORWARD_MESSAGE = ...
    COPY_MESSAGE = ...
    SEND_PHOTO = ...
    SEND_AUDIO = ...
    SEND_DOCUMENT = ...
    SEND_VIDEO = ...
    SEND_ANIMATION = ...
    SEND_VOICE = ...
    SEND_VIDEO_NOTE = ...
    SEND_MEDIA_GROUP = ...
    SEND_LOCATION = ...
    EDIT_MESSAGE_LIVE_LOCATION = ...
    STOP_MESSAGE_LIVE_LOCATION = ...
    SEND_VENUE = ...
    SEND_CONTACT = ...
    SEND_POLL = ...
    SEND_DICE = ...
    SEND_CHAT_ACTION = ...
    GET_USER_PROFILE_PHOTOS = ...
    GET_FILE = ...
    KICK_CHAT_MEMBER = ...
    BAN_CHAT_MEMBER = ...
    UNBAN_CHAT_MEMBER = ...
    RESTRICT_CHAT_MEMBER = ...
    PROMOTE_CHAT_MEMBER = ...
    SET_CHAT_ADMINISTRATOR_CUSTOM_TITLE = ...
    BAN_CHAT_SENDER_CHAT = ...
    UNBAN_CHAT_SENDER_CHAT = ...
    SET_CHAT_PERMISSIONS = ...
    EXPORT_CHAT_INVITE_LINK = ...
    CREATE_CHAT_INVITE_LINK = ...
    EDIT_CHAT_INVITE_LINK = ...
    REVOKE_CHAT_INVITE_LINK = ...
    APPROVE_CHAT_JOIN_REQUEST = ...
    DECLINE_CHAT_JOIN_REQUEST = ...
    SET_CHAT_PHOTO = ...
    DELETE_CHAT_PHOTO = ...
    SET_CHAT_TITLE = ...
    SET_CHAT_DESCRIPTION = ...
    PIN_CHAT_MESSAGE = ...
    UNPIN_CHAT_MESSAGE = ...
    UNPIN_ALL_CHAT_MESSAGES = ...
    LEAVE_CHAT = ...
    GET_CHAT = ...
    GET_CHAT_ADMINISTRATORS = ...
    GET_CHAT_MEMBER_COUNT = ...
    GET_CHAT_MEMBERS_COUNT = ...
    GET_CHAT_MEMBER = ...
    SET_CHAT_STICKER_SET = ...
    DELETE_CHAT_STICKER_SET = ...
    GET_FORUM_TOPIC_ICON_STICKERS = ...
    CREATE_FORUM_TOPIC = ...
    EDIT_FORUM_TOPIC = ...
    CLOSE_FORUM_TOPIC = ...
    REOPEN_FORUM_TOPIC = ...
    DELETE_FORUM_TOPIC = ...
    UNPIN_ALL_FORUM_TOPIC_MESSAGES = ...
    EDIT_GENERAL_FORUM_TOPIC = ...
    CLOSE_GENERAL_FORUM_TOPIC = ...
    REOPEN_GENERAL_FORUM_TOPIC = ...
    HIDE_GENERAL_FORUM_TOPIC = ...
    UNHIDE_GENERAL_FORUM_TOPIC = ...
    ANSWER_CALLBACK_QUERY = ...
    SET_MY_COMMANDS = ...
    DELETE_MY_COMMANDS = ...
    GET_MY_COMMANDS = ...
    EDIT_MESSAGE_TEXT = ...
    EDIT_MESSAGE_CAPTION = ...
    EDIT_MESSAGE_MEDIA = ...
    EDIT_MESSAGE_REPLY_MARKUP = ...
    STOP_POLL = ...
    DELETE_MESSAGE = ...
    SEND_STICKER = ...
    GET_STICKER_SET = ...
    UPLOAD_STICKER_FILE = ...
    GET_CUSTOM_EMOJI_STICKERS = ...
    CREATE_NEW_STICKER_SET = ...
    ADD_STICKER_TO_SET = ...
    SET_STICKER_POSITION_IN_SET = ...
    DELETE_STICKER_FROM_SET = ...
    SET_STICKER_SET_THUMB = ...
    ANSWER_INLINE_QUERY = ...
    ANSWER_WEB_APP_QUERY = ...
    SET_CHAT_MENU_BUTTON = ...
    GET_CHAT_MENU_BUTTON = ...
    SET_MY_DEFAULT_ADMINISTRATOR_RIGHTS = ...
    GET_MY_DEFAULT_ADMINISTRATOR_RIGHTS = ...
    SEND_INVOICE = ...
    CREATE_INVOICE_LINK = ...
    ANSWER_SHIPPING_QUERY = ...
    ANSWER_PRE_CHECKOUT_QUERY = ...
    SET_PASSPORT_DATA_ERRORS = ...
    SEND_GAME = ...
    SET_GAME_SCORE = ...
    GET_GAME_HIGH_SCORES = ...


