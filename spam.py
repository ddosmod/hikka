from asyncio import sleep, gather
from .. import loader, utils

def register(cb):
    cb(SpamMod())

class SpamMod(loader.Module):
    """Спам модуль разработан автором @ddospacket"""

    strings = {"name": "Spam"}

    async def spamcmd(self, message):
        """Спамит указанное количество сообщений. Используй .spam <кол-во:int> <текст или реплай>."""
        try:
            await message.delete()
            args = utils.get_args(message)
            count = int(args[0].strip())
            for _ in range(count):
                await message.respond(" ".join(args[1:]))
        except Exception as e:
            await message.client.send_message(
                message.to_id, f"Ошибка: {str(e)}\nИспользуйте .stopspam только в критических ситуациях."
            )

    async def stopspamcmd(self, message):
        """Отключить спам в случае ошибки или критической ситуации."""
        self.all_tasks_cancel()
        await message.client.send_message(message.to_id, "Спам остановлен в связи с критической ситуацией.")
