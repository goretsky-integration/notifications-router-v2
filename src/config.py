import pathlib
import tomllib

from pydantic import BaseModel, HttpUrl, SecretStr

__all__ = ('Config', 'get_config', 'CONFIG_FILE_PATH')

CONFIG_FILE_PATH = pathlib.Path(__file__).parent.parent / 'config.toml'


class Config(BaseModel):
    units_storage_base_url: HttpUrl
    telegram_bot_token: SecretStr


def get_config() -> Config:
    config = CONFIG_FILE_PATH.read_text(encoding='utf-8')
    config = tomllib.loads(config)

    return Config(
        units_storage_base_url=(
            config['external_services_api']['units_storage_base_url']
        ),
        telegram_bot_token=config['telegram_bot']['token'],
    )
