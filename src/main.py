from faststream import FastStream
from faststream.rabbit import RabbitBroker

from handlers import router


broker = RabbitBroker('amqp://localhost:5672/')
app = FastStream(broker)
broker.include_router(router)
