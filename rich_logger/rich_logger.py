import configparser
import logging
from logging.handlers import RotatingFileHandler

from rich.console import Console
from rich.logging import RichHandler

from rich_logger.console_logger_highlighter import ConsoleLoggerHighlighter
from rich_logger.defaults import DEFAULT_LOG_CONFIG, DEFAULT_RICH_STYLE
from rich_logger.utils import get_date_as_regex


class RichLogger:
    def __init__(
        self,
        logger_configuration_file: str = "",
        logger_name: str = "rich_logger",
        logging_to_console: bool = True,
        logging_to_file: bool = False,
        logging_file_name: str = "rich_logger.log",
    ):
        """
        Initialize the RichLogger instance.
        Args:
            logger_configuration_file (str, optional): Path to the logger configuration file. Defaults to "".
            logger_name (str, optional): Name of the logger. Defaults to "rich_logger".
            logging_to_console (bool, optional): Flag to enable logging to console. Defaults to True.
            logging_to_file (bool, optional): Flag to enable logging to a file. Defaults to False.
            logging_file_name (str, optional): Name of the log file. Defaults to "rich_logger.log".
        """

        user_configuration = {}
        # Load the given configuration file
        if len(logger_configuration_file) > 0:
            parser = configparser.ConfigParser()
            parser.read(logger_configuration_file)
            user_configuration = {
                key: parser.get("logging", key, fallback=None) for key in parser["logging"]
            }

        self.merged_configurations = {**DEFAULT_LOG_CONFIG, **user_configuration}
        self.merged_rich_styles = {**DEFAULT_RICH_STYLE, **{logger_name: "bold black"}}
        self.regex_time_format = get_date_as_regex(self.merged_configurations["date_format"])

        self.logger = logging.getLogger(logger_name)
        self.formatter = logging.Formatter(
            self.merged_configurations["logger_format"],
            datefmt=self.merged_configurations["date_format"],
        )
        self.plain_formatter = logging.Formatter(
            self.merged_configurations["logger_format"],
            datefmt=self.merged_configurations["date_format"],
        )
        self.logger.setLevel(self.merged_configurations["level"])

        if not self.logger.hasHandlers():
            self._set_up_file_logger(logging_to_file, logging_file_name)
            self._set_up_console_logger(logging_to_console)
        else:
            self._retrieve_file_handler()
            self._retrieve_console_handler()

    def _retrieve_file_handler(self):
        self.file_handler = next(
            (
                handler
                for handler in self.logger.handlers
                if isinstance(handler, RotatingFileHandler)
            ),
            None,
        )

    def _retrieve_console_handler(self):
        self.console_handler = next(
            (handler for handler in self.logger.handlers if isinstance(handler, RichHandler)), None
        )

    def _set_up_file_logger(self, logging_to_file: bool, logging_file_name: str):
        if logging_to_file:
            self.file_handler = RotatingFileHandler(
                logging_file_name,
                maxBytes=self.merged_configurations["max_bytes"],
                backupCount=self.merged_configurations["backup_count"],
            )
            self.file_handler.setFormatter(self.plain_formatter)
            self.logger.addHandler(self.file_handler)
        else:
            self.file_handler = logging.NullHandler()
            self.logger.addHandler(self.file_handler)

    def _set_up_console_logger(self, logging_to_console: bool):
        if logging_to_console:
            self.console_handler = RichHandler(
                console=Console(),
                level=self.merged_configurations["level"],
                show_level=False,
                show_time=False,
                show_path=False,
                highlighter=ConsoleLoggerHighlighter(
                    keywords_n_styles=self.merged_rich_styles,
                    regex_time_format=self.regex_time_format,
                ),
            )
            self.console_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.console_handler)
        else:
            self.console_handler = logging.NullHandler()
            self.logger.addHandler(self.console_handler)

    def __getattr__(self, name):
        """Delegate method calls to the logger instance."""
        return getattr(self.logger, name)
