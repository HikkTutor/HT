__version__ = (1, 0, 0)

#            © Copyright 2025
#           https://t.me/HikkTutor 
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
#┏┓━┏┓━━┏┓━━┏┓━━┏━━━━┓━━━━━┏┓━━━━━━━━━━━━
#┃┃━┃┃━━┃┃━━┃┃━━┃┏┓┏┓┃━━━━┏┛┗┓━━━━━━━━━━━
#┃┗━┛┃┏┓┃┃┏┓┃┃┏┓┗┛┃┃┗┛┏┓┏┓┗┓┏┛┏━━┓┏━┓━━━━
#┃┏━┓┃┣┫┃┗┛┛┃┗┛┛━━┃┃━━┃┃┃┃━┃┃━┃┏┓┃┃┏┛━━━━
#┃┃━┃┃┃┃┃┏┓┓┃┏┓┓━┏┛┗┓━┃┗┛┃━┃┗┓┃┗┛┃┃┃━━━━━
#┗┛━┗┛┗┛┗┛┗┛┗┛┗┛━┗━━┛━┗━━┛━┗━┛┗━━┛┗┛━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# load from: t.me:HikkTutor 
# meta developer:@HikkTutor 
# author: vsakoe
# name: WinKey

import random
import asyncio
from .. import loader, utils

@loader.tds
class WinKey(loader.Module):
    """Активация любой Windows"""

    strings = {"name": "WinKey"}

    async def wkeycmd(self, message):
        """- генерация глюча Windows"""
        self.windows_versions = [
            "Windows 7 Home",
            "Windows 7 Professional",
            "Windows 8 Home",
            "Windows 8 Professional",
            "Windows 10 Home",
            "Windows 10 Pro",
            "Windows 11 Home",
            "Windows 11 Pro",
            "Windows 11 Education"
        ]

        self.prank_messages = [
            "<b>Ошибка:</b> я ключ где-то потерял, сорян.",
            "<b>Окак:</b> не нашёл ничего.",
            "<b>Ошибка:</b> Вы должны быть подписаны на @HikkTutor более 40 лет для использования модуля.",
            "А хер тебе, с 1 апреля!",
            "Ой, автор модуля стырил ключ по дороге."
        ]

        await self.inline.form(
            text="Выберите операционную систему для активации:",
            message=message,
            reply_markup=[
                [{"text": version, "callback": self.process_selection, "args": (version,)}] for version in self.windows_versions
            ]
        )

    async def process_selection(self, call, version):
        await call.edit(f"🔄 Начинаю генерацию ключа для {version}...")

        steps = [
            "🔍 Сбор системной информации...",
            "🔄 Подключение к серверу активации...",
            "🔗 Запрос ключа...",
            "🔄 Проверка совместимости...",
            "🔍 Завершающая проверка..."
        ]

        for step in steps:
            await asyncio.sleep(random.uniform(1.5, 5.0))
            await call.edit(step)

        fake_key = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        validity_period = random.choice(["1 час", "1 день", "3 дня", "1 неделя"])

        await call.edit(
            f"🔑 <b>Ключ:</b> {fake_key}\n"
            f"📅 <b>Актуален:</b> {validity_period}\n"
            f"💻 <b>Операционная система:</b> {version}"
        )

        await asyncio.sleep(1)

        prank_message = random.choice(self.prank_messages)
        await call.edit(prank_message)