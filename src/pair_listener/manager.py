import json
from typing import Awaitable, Callable

import aiohttp
import aiojobs

from .schemas import Candlestick

WSManagerHandler = Callable[[Candlestick], Awaitable[None]]


async def default_handler(candlestick: Candlestick):
    print(f"[{candlestick.pair}]", candlestick)


class WSManager:
    """Websocket Manager for listen coin pair changes."""

    def __init__(
        self,
        handler: WSManagerHandler = default_handler,
    ):
        self.template = "wss://stream.binance.com:9443/ws/{pair}@kline_1m"
        self.tasks = dict()
        self.handler = handler

    async def init_schedulers(self):
        self.listener_scheduler = await aiojobs.create_scheduler()
        self.handler_scheduler = await aiojobs.create_scheduler()

    async def start_listener(self, pair: str):
        uri = self.template.format(pair=pair)
        session = aiohttp.ClientSession()
        async with session.ws_connect(uri) as websocket:
            async for message in websocket:
                data = json.loads(message.data)
                candlestick = Candlestick(**data["k"])
                await self.handler_scheduler.spawn(self.handler(candlestick))

    async def run(self, pair: str):
        task = await self.listener_scheduler.spawn(self.start_listener(pair))
        self.tasks[pair] = task

    async def stop(self, pair: str):
        # TODO fix pls
        task = self.tasks.get(pair)
        await task.close()
        self.tasks.pop(pair)

    async def get_listeners(self):
        return self.tasks

    async def get_handler_jobs(self):
        return self.handler_scheduler._jobs
