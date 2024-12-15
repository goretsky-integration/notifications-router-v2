import humanize.i18n
import sentry_sdk
import structlog
from fast_depends import Depends, inject
from faststream import FastStream
from faststream.rabbit import RabbitBroker

import handlers
from config import Config, get_config
from logger import init_logging

logger = structlog.get_logger('app')

humanize.i18n.activate("ru_RU")


def on_startup() -> None:
    init_logging()
    init_sentry()


@inject
def init_sentry(config: Config = Depends(get_config, use_cache=True)) -> None:
    if config.sentry.is_enabled:
        sentry_sdk.init(
            dsn=config.sentry.dsn.get_secret_value(),
            traces_sample_rate=config.sentry.traces_sample_rate,
            profiles_sample_rate=config.sentry.profiles_sample_rate,
        )


broker = RabbitBroker('amqp://localhost:5672/', logger=logger)
app = FastStream(broker, logger=logger)
app.on_startup(on_startup)
broker.include_routers(
    handlers.specific_chats.router,
    handlers.specific_units.router,
)
