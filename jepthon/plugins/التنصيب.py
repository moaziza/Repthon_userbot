from telethon import events
import random, re
from jepthon.utils import admin_cmd
import asyncio 

@borg.on(admin_cmd("تنصيب السورس"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌁︙**اهـلا بك فـي تنصيب السورس** \n⌁︙[اضغـط هنـا](https://dashboard.heroku.com/new?template=https://github.com/mostafaaziza/tilthiyun)رابط التنصيب(⌁︙ يرجى متابعة قناة العزايزي الرسمية لتنصيب السورس - @BANDA1M)\n⌁︙قناة السورس - @BANDA1M")
