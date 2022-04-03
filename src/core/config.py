from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):

    # Tg webhook settings
    API_TOKEN: str
    WEBHOOK_HOST: HttpUrl
    WEBHOOK_PATH: str = '/telegram/webhook'

    @property
    def WEBHOOK_URL(self) -> HttpUrl:
        return f'{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}'

    class Config:
        case_sensitive = True
        env_file = ".env"



settings = Settings()
