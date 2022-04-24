from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart


async def cmd_start_handler(message: types.Message):
    await message.answer("Приветствие")


def init_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start_handler, CommandStart())
