from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from src.database.connection import sessionmaker
from src.database.repositories import users


class ACLMiddleware(BaseMiddleware):
    async def setup_chat(
        self,
        data: dict,
        user: types.User,
        chat: types.Chat | None = None,
    ):
        # TODO вынести sessionmaker
        data["user"] = await users.get_or_create_user(sessionmaker(), user)

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message.chat)

    async def on_pre_process_callback_query(
        self,
        query: types.CallbackQuery,
        data: dict,
    ):
        await self.setup_chat(
            data,
            query.from_user,
            query.message.chat if query.message else None,
        )
