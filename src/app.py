from aiohttp import web
from src.bot import TelegramWebhookView, init_dispatcher
from src.core.config import settings


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def init_app() -> web.Application:
    app = web.Application()
    app['BOT_DISPATCHER'] = await init_dispatcher()

    app.router.add_route('GET', '/', handle)
    app.router.add_route('*', settings.WEBHOOK_PATH, TelegramWebhookView, name='webhook_handler')

    return app

if __name__ == '__main__':
    web.run_app(init_app(), port=8000)
