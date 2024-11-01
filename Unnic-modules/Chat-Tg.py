#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ© Copyright 2024
#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤhttps://t.me/unnic
# 🔒ㅤㅤㅤㅤㅤLicensed under the GNU AGPLv3
# 🌐ㅤㅤhttps://www.gnu.org/licenses/agpl-3.0.html
import io
import asyncio
from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
from .. import loader, utils

@loader.tds
class БылMod(loader.Module):
    """Модуль для групп"""

    strings = {
        "name": "Был"
    }

    def init(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client: TelegramClient, db):
        self._db = db
        self._client = client
        
    async def логcmd(self, message: Message):
        """Прежде чем, прочти инструкцию"""
        if not message.chat:
            await message.edit("<emoji document_id=5443055905836903328>❗️</emoji> <b>Ошибка!</b>")
            return
        chat = message.chat

        f = io.BytesIO()
        f.name = f"Chat Dump {chat.id}.csv"
        f.write("FNAME;LNAME;USER;ID;NUMBER\n".encode())
        me = await message.client.get_me()
        for i in await message.client.get_participants(message.to_id):
            if i.id == me.id:
                continue
            f.write(
                f"{str(i.first_name)};{str(i.last_name)};{str(i.username)};{str(i.id)};{str(i.phone)}\n".encode()
            )
        f.seek(0)
        await message.client.send_file("me", f, caption="ID Чата: " + str(chat.id))

        await message.edit("<b><emoji document_id=5445156432607454501>✅</emoji> Сделал то что ты хотел, лог в избранном.</b>")
        f.close()

    async def иcmd(self, message: Message):
        """Показать ID пользователя"""
        args = utils.get_args_raw(message)

        if message.is_reply:
            reply_message = await message.get_reply_message()
            user = await message.client.get_entity(reply_message.sender_id)
        elif args:
            try:
                user = await message.client.get_entity(args)
            except ValueError:
                await message.edit("<b>Ошибка</b>")
                return
        else:
            user = await message.get_sender()

        user_initials = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.first_name
        user_id = user.id
        await message.edit(f'<emoji document_id=5445109840802227336>🛫</emoji> <a href="tg://openmessage?user_id={user_id}"><b>{user_initials}</b></a>\n<emoji document_id=5442848669369903303>📧</emoji> <code>@{user_id}</code>')

    async def тегcmd(self, message: Message):
        """Тегает всех админов чата, игнорируя ботов"""
        if not message.chat:
            await message.edit("<b>Ошибка!</b>")
            return

        chat = message.chat
        admins = await message.client.get_participants(chat, filter=ChannelParticipantsAdmins)

        real_admins = [admin for admin in admins if not admin.bot]

        if not real_admins:
            await message.edit("<b>Нет админов в этом чате.</b>")
            return

        admin_mentions = [f"<a href='tg://user?id={admin.id}'>.</a>" for admin in real_admins]

        await message.edit(" ".join(admin_mentions))
        
    async def хелпcmd(self, message: Message):
        """Показать информацию по команде .лог"""
        instruction = (
            "<b>Информация:\n\n"
            "<emoji document_id=5442796494107191902>🔓</emoji> Команда <code>.лог</code> выполняет дамп чата, создавая файл, содержащий список всех участников, "
            "и отправляет его в «Избранное». Это полезно для архивирования и анализа данных о пользователях чата.</b>\n"
        )

        sent_message = await self._client.send_message(message.chat_id, instruction)

        await asyncio.sleep(10)
        await sent_message.delete()

# Пашёл нахуй
