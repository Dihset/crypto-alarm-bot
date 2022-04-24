from aiogram import Dispatcher

from .start import init_handlers as init_start_handlers


def init_handlers(dp: Dispatcher):
    init_start_handlers(dp)
