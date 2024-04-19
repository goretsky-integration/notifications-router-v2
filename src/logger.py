import logging

import structlog
from faststream import context
from structlog.contextvars import merge_contextvars
from structlog_sentry import SentryProcessor

__all__ = ('init_logging',)


def merge_extra_contextvars(
        logger: structlog.types.WrappedLogger,
        method_name: str,
        event_dict: structlog.types.EventDict,
) -> structlog.types.EventDict:
    event_dict["extra"] = event_dict.get(
        "extra",
        context.get_local("log_context") or {},
    )
    return event_dict


def init_logging() -> None:
    processors = (
        merge_contextvars,
        merge_extra_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.dict_tracebacks,
        SentryProcessor(event_level=logging.WARNING),
        structlog.processors.JSONRenderer(),
    )
    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=False,
    )
