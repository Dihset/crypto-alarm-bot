from aiogram import Bot, types, Dispatcher
from src.core.config import settings


async def echo(message: types.Message):
    return await message.answer(message.text)


async def init_dispatcher():
    bot = Bot(token=settings.API_TOKEN)
    await bot.set_webhook(settings.WEBHOOK_URL)
    dispatcher = Dispatcher(bot)

    dispatcher.register_message_handler(echo)

    return dispatcher
