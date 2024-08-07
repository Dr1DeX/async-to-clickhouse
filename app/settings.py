from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 9000
    DB_USER: str = 'user'
    DB_PASSWORD: str = 'password'
    DB_NAME: str = 'test-db'
    DB_DRIVER: str = 'clickhouse+httpx'

    @property
    def db_url(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
