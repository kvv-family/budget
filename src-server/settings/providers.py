from pydantic_settings import BaseSettings


class ProvidersSettings(BaseSettings):
    locale_protocol: str = "http"
    locale_host: str = "localhost"
    locale_port: int = 8000
    