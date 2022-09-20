#h
import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


@zedub.zed_cmd(
    pattern="ساوند(?:\s|$)([\s\S]*)",
    command=("ساوند", plugin_category),
    info={
        "header": "لتحميل الاغاني من ساوند كلاود عبر الرابـط",
        "الاستـخـدام": "{tr}ساوند بالـرد ع رابـط",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```- رد ع الرابط اول شي حب .```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```- رد ع الرابط اول شي حب .```**")
        return
    chat = "@DeezerMusicBot"
    catevent = await edit_or_reply(event, "**- جار التحميل من ساوند كلاود انتضر .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=595898211)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**- تحقق من انك لم تقة بحظر البوت : @downloader_tiktok_bot ثم اعد استخدام الامر .**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**😂🈲**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(
    pattern="كلاود ([\s\S]*)",
    command=("كلاود", plugin_category),
    info={
        "header": "لتحميل الاغاني من ساوند كلاود عبر الرابـط",
        "الاستـخـدام": "{tr}كلاود + رابط",
    },
)
async def zed(event):
    if event.fwd_from:
        return
    jepiq = event.pattern_match.group(1)
    jepiq = "@DeezerMusicBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(jepiq, jepiq)
    await tap[0].click(event.chat_id)
    await event.delete()
