from aiogram import Bot, Dispatcher

from src.core.config import settings

from .handlers import init_handlers
from .middlewares import ACLMiddleware


async def init_dispatcher():
    bot = Bot(token=settings.API_TOKEN)
    await bot.set_webhook(settings.WEBHOOK_URL)

    dispatcher = Dispatcher(bot)
    dispatcher.middleware.setup(ACLMiddleware())
    init_handlers(dispatcher)

    return dispatcher
