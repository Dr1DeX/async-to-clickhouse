from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 9000
    DB_USER: str = 'default'
    DB_PASSWORD: str = ''
    DB_NAME: str = 'test_db'
    DB_DRIVER: str = 'clickhouse+native'
