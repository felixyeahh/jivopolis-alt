"""
This type stub file was generated by pyright.
"""

import datetime
import typing
from . import base
from .user import User
from ..utils import helper

T = typing.TypeVar('T')
class ChatMemberStatus(helper.Helper):
    """
    Chat member status
    """
    mode = ...
    CREATOR = ...
    OWNER = ...
    ADMINISTRATOR = ...
    MEMBER = ...
    RESTRICTED = ...
    LEFT = ...
    KICKED = ...
    BANNED = ...
    @classmethod
    def is_chat_creator(cls, role: str) -> bool:
        ...
    
    is_chat_owner = ...
    @classmethod
    def is_chat_admin(cls, role: str) -> bool:
        ...
    
    @classmethod
    def is_chat_member(cls, role: str) -> bool:
        ...
    
    @classmethod
    def get_class_by_status(cls, status: str) -> typing.Optional[typing.Type[ChatMember]]:
        ...
    


class ChatMember(base.TelegramObject):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:
        ChatMemberOwner
        ChatMemberAdministrator
        ChatMemberMember
        ChatMemberRestricted
        ChatMemberLeft
        ChatMemberBanned

    https://core.telegram.org/bots/api#chatmember
    """
    status: base.String = ...
    user: User = ...
    def __int__(self) -> int:
        ...
    
    @classmethod
    def resolve(cls, **kwargs) -> typing.Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]:
        ...
    
    @classmethod
    def to_object(cls, data: typing.Dict[str, typing.Any], conf: typing.Dict[str, typing.Any] = ...) -> typing.Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]:
        ...
    
    def is_chat_creator(self) -> bool:
        ...
    
    is_chat_owner = ...
    def is_chat_admin(self) -> bool:
        ...
    
    def is_chat_member(self) -> bool:
        ...
    


class ChatMemberOwner(ChatMember):
    """
    Represents a chat member that owns the chat and has all
    administrator privileges.
    https://core.telegram.org/bots/api#chatmemberowner
    """
    status: base.String = ...
    user: User = ...
    custom_title: base.String = ...
    is_anonymous: base.Boolean = ...
    can_be_edited: base.Boolean = ...
    can_manage_chat: base.Boolean = ...
    can_post_messages: base.Boolean = ...
    can_edit_messages: base.Boolean = ...
    can_delete_messages: base.Boolean = ...
    can_manage_voice_chats: base.Boolean = ...
    can_manage_video_chats: base.Boolean = ...
    can_restrict_members: base.Boolean = ...
    can_promote_members: base.Boolean = ...
    can_change_info: base.Boolean = ...
    can_invite_users: base.Boolean = ...
    can_pin_messages: base.Boolean = ...
    can_manage_topics: base.Boolean = ...


class ChatMemberAdministrator(ChatMember):
    """
    Represents a chat member that has some additional privileges.

    https://core.telegram.org/bots/api#chatmemberadministrator
    """
    status: base.String = ...
    user: User = ...
    can_be_edited: base.Boolean = ...
    custom_title: base.String = ...
    is_anonymous: base.Boolean = ...
    can_manage_chat: base.Boolean = ...
    can_post_messages: base.Boolean = ...
    can_edit_messages: base.Boolean = ...
    can_delete_messages: base.Boolean = ...
    can_manage_voice_chats: base.Boolean = ...
    can_manage_video_chats: base.Boolean = ...
    can_restrict_members: base.Boolean = ...
    can_promote_members: base.Boolean = ...
    can_change_info: base.Boolean = ...
    can_invite_users: base.Boolean = ...
    can_pin_messages: base.Boolean = ...
    can_manage_topics: base.Boolean = ...


class ChatMemberMember(ChatMember):
    """
    Represents a chat member that has no additional privileges or
    restrictions.

    https://core.telegram.org/bots/api#chatmembermember
    """
    status: base.String = ...
    user: User = ...


class ChatMemberRestricted(ChatMember):
    """
    Represents a chat member that is under certain restrictions in the
    chat. Supergroups only.

    https://core.telegram.org/bots/api#chatmemberrestricted
    """
    status: base.String = ...
    user: User = ...
    is_member: base.Boolean = ...
    can_change_info: base.Boolean = ...
    can_invite_users: base.Boolean = ...
    can_pin_messages: base.Boolean = ...
    can_manage_topics: base.Boolean = ...
    can_send_messages: base.Boolean = ...
    can_send_audios: base.Boolean = ...
    can_send_documents: base.Boolean = ...
    can_send_photos: base.Boolean = ...
    can_send_videos: base.Boolean = ...
    can_send_video_notes: base.Boolean = ...
    can_send_voice_notes: base.Boolean = ...
    can_send_media_messages: base.Boolean = ...
    can_send_polls: base.Boolean = ...
    can_send_other_messages: base.Boolean = ...
    can_add_web_page_previews: base.Boolean = ...
    until_date: datetime.datetime = ...


class ChatMemberLeft(ChatMember):
    """
    Represents a chat member that isn't currently a member of the chat,
    but may join it themselves.

    https://core.telegram.org/bots/api#chatmemberleft
    """
    status: base.String = ...
    user: User = ...


class ChatMemberBanned(ChatMember):
    """
    Represents a chat member that was banned in the chat and can't
    return to the chat or view chat messages.

    https://core.telegram.org/bots/api#chatmemberbanned
    """
    status: base.String = ...
    user: User = ...
    until_date: datetime.datetime = ...


