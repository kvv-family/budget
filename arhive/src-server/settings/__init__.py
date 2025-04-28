from pydantic_settings import BaseSettings
from .providers import ProvidersSettings

class SettingsModel(ProvidersSettings, BaseSettings): ...


settings = SettingsModel()