import logging

DEFAULT_LOG_CONFIG = {
    "level": logging.DEBUG,
    "logger_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "max_bytes": 1000000,
    "backup_count": 5,
}
