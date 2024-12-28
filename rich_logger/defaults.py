import logging

DEFAULT_LOG_CONFIG = {
    "log_level": logging.DEBUG,
    "logger_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "max_bytes": 1000000,
    "backup_count": 5,
}


DEFAULT_RICH_STYLE = {
    "DEBUG": "bold green",
    "INFO": "bold blue",
    "WARNING": "bold yellow",
    "ERROR": "bold red",
    "CRITICAL": "bold red underline",
    "TIME": "cyan",
}
