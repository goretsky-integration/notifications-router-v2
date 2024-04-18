import sentry_sdk
from fast_depends import Depends
from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config import Config, get_config
from handlers import router


def init_sentry(config: Config = Depends(get_config, use_cache=True)) -> None:
    if config.sentry.is_enabled:
        sentry_sdk.init(
            dsn=config.sentry.dsn.get_secret_value(),
            traces_sample_rate=config.sentry.traces_sample_rate,
            profiles_sample_rate=config.sentry.profiles_sample_rate,
        )


broker = RabbitBroker('amqp://localhost:5672/')
app = FastStream(broker)
app.on_startup(init_sentry)
broker.include_router(router)
