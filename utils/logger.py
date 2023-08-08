from loguru import logger

logger.add(
    "kscincident.log",
    retention="7 days",
    # format="{time:DD.MM HH:mm:ss}|{level}|{message}",
    # colorize=True,
    backtrace=True,
    diagnose=True,
    enqueue=True,
    encoding="utf-8",
)
