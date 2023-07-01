import contextlib
from ... import bot, tglog

from ...misc import get_embedded_link
from ...database import cur, insert_clan
from ..start import StartCommand

from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.utils.exceptions import BadRequest


async def create_clan(call: CallbackQuery) -> None:
    '''
    Callback for clan creating.

    :param call - callback:
    '''
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    member = await bot.get_chat_member(chat_id, user_id)

    if (
        not member.is_chat_admin()
        and not member.is_chat_creator()
    ):
        return await bot.send_message(
            chat_id,
            '👀 <i>Создать клан может только администратор чата</i>'
        )

    count = cur.select("count(*)", "clandata").where(clan_id=chat_id).one()

    if count >= 1:
        return await bot.send_message(
            chat_id,
            '<i>🚥 Такой клан уже существует. Для создания нового сначала'
            ' удалите старый.</i>'
        )
    try:
        link = await insert_clan(call.message.chat, call.from_user)
    except BadRequest as e:
        if str(e) == 'Not enough rights to manage chat invite link':
            await call.message.edit_text(
                f"{call.message.text}\n\n>>>🚨 Пожалуйста, сначала дайте боту "
                "административные права."
            )
        else:
            raise

    await tglog(
        (
            f"🏘 #new_clan | {await get_embedded_link(user_id)}"
            f" создал новый клан: <a href='{link}'>{call.message.chat.title}"
            f"</a>. <code>[{chat_id}]</code>"
        )
    )
    await bot.send_message(
        chat_id,
        text=(
            f"<i>🏘 {await get_embedded_link(user_id)} создал новый клан. "
            "Скорее присоединяйтесь!</i>"
        ),
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton('➕ Присоединиться', callback_data='join_clan')
        )
    )

    await StartCommand()._clan_start(call.message.chat)


async def joinclan(call: CallbackQuery, user_id: int) -> None:
    '''
    Callback for clan joining

    :param call - callback:
    :param user_id:
    '''
    chat_id = call.message.chat.id

    count = cur.select("count(*)", "clandata").where(clan_id=chat_id).one()

    if count < 1:
        return await call.answer(
            "😓 Похоже, такого клана не существует.",
            show_alert=True
        )
    elif count > 1:
        raise ValueError("found more than one clan with such ID")

    user_clan = cur.select("clan_id", "userdata").where(user_id=user_id).one()

    if not user_clan or user_clan != chat_id:
        cur.update("userdata").set(clan_id=chat_id).where(
            user_id=user_id).commit()
        await bot.send_message(
            chat_id,
            f'<i><b>{await get_embedded_link(user_id)}</b> присоединился к '
            'клану</i>'
        )

        if user_clan:
            with contextlib.suppress(Exception):
                await bot.send_message(
                    user_clan,
                    f"<i><b>{await get_embedded_link(user_id)}</b> вышел из"
                    " клана</i>"
                )
    else:
        cur.update("userdata").set(
            clan_id=None).where(user_id=user_id).commit()
        await bot.send_message(
            chat_id,
            f"<i><b>{await get_embedded_link(user_id)}</b> вышел из клана</i>"
        )


async def leaveclan(call: CallbackQuery) -> None:
    """
    Callback for leave clan

    :param call - callback:
    """
    user_id = call.from_user.id
    user_clan = cur.select("clan_id", "userdata").where(user_id=user_id).one()

    if not user_clan or user_clan != call.message.chat.id:
        return await call.answer(
            "🤥 Но ты ведь не состоишь в этом клане… Нельзя выйти если ты не "
            "заходил, дорогой!",
            show_alert=True
        )

    cur.update("userdata").set(clan_id=None).where(
        user_id=user_id).commit()

    await call.message.answer(
        f"<i><b>{await get_embedded_link(user_id)}</b> вышел из клана</i>")
