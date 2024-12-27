import configparser
import logging

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
    ):

        user_configuration = {}
        # Load the given configuration file
        if len(logger_configuration_file) > 0:
            parser = configparser.ConfigParser()
            parser.read(logger_configuration_file)
            user_configuration = {
                key: parser.get("logging", key, fallback=None) for key in parser["logging"]
            }

        merged_configurations = {**DEFAULT_LOG_CONFIG, **user_configuration}
        merged_rich_styles = {**DEFAULT_RICH_STYLE, **{logger_name: "bold black"}}
        regex_time_format = get_date_as_regex(merged_configurations["date_format"])

        self.logger = logging.getLogger(logger_name)
        self.formatter = logging.Formatter(
            merged_configurations["logger_format"],
            datefmt=merged_configurations["date_format"],
        )
        self.logger.setLevel(merged_configurations["level"])

        if not self.logger.hasHandlers():
            if logging_to_console:
                self.console_handler = RichHandler(
                    console=Console(),
                    level=merged_configurations["level"],
                    show_level=False,
                    show_time=False,
                    show_path=False,
                    highlighter=ConsoleLoggerHighlighter(
                        keywords_n_styles=merged_rich_styles,
                        regex_time_format=regex_time_format,
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
