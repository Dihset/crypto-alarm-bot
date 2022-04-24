from pydantic import BaseSettings, HttpUrl, PostgresDsn


class Settings(BaseSettings):

    # Tg webhook settings
    API_TOKEN: str
    WEBHOOK_HOST: HttpUrl
    WEBHOOK_PATH: str = "/telegram/webhook"

    @property
    def WEBHOOK_URL(self) -> HttpUrl:
        return f"{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}"

    # Postgres settings
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    @property
    def SQLALCHEMY_PG_URI(self) -> PostgresDsn:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def ALEMBIC_PG_URI(self) -> PostgresDsn:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
