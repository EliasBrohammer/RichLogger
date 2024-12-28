import configparser
import unittest

from rich_logger.rich_logger import RichLogger
from rich_logger.utils import get_date_as_regex


class TestRichLoggerImport(unittest.TestCase):
    def test_import_works(self):
        """Test if the RichLogger class can be imported without errors."""
        logger = RichLogger()
        self.assertIsInstance(logger, RichLogger, "RichLogger should be an instance of its class.")

    def test_console_logger(self):
        """Test if the console logger is created without errors."""
        logger = RichLogger(
            logger_name="console_logger", logging_to_console=True, logging_to_file=False
        )
        self.assertIsNotNone(logger.console_handler, "Console logger should be created.")

    def test_file_logger(self):
        """Test if the file logger is created without errors when enabled."""
        logger = RichLogger(
            logger_name="file_logger", logging_to_console=False, logging_to_file=True
        )
        self.assertIsNotNone(
            logger.file_handler, "File logger should be created when logging_to_file is True."
        )

    def test_null_logger(self):
        """Test if the null logger is created without errors when disabled."""
        logger = RichLogger(
            logger_name="null_logger", logging_to_console=False, logging_to_file=False
        )
        self.assertIsNotNone(
            logger.file_handler, "Null logger should be created when logging_to_file is False."
        )
        self.assertIsNotNone(
            logger.console_handler,
            "Null logger should be created when logging_to_console is False.",
        )

    def test_console_output(self):
        """Test if the console logger is logging without errors."""
        logger = RichLogger(
            logger_name="console_logger", logging_to_console=True, logging_to_file=False
        )
        logger.info("Test message")

    def test_configuration_file(self):
        """Test if the logger configuration file is loaded without errors."""

        file = "tests/test_configuration.ini"
        logger = RichLogger(logger_configuration_file=file)

        # manually read the configuration file
        parser = configparser.ConfigParser()
        parser.read(file)
        log_level = parser.get("logging", "log_level", fallback=None)
        max_bytes = parser.get("logging", "max_bytes", fallback=None)
        self.assertEqual(
            logger.merged_configurations["log_level"],
            log_level,
            "Logger should be created with configuration file.",
        )
        self.assertEqual(
            logger.merged_configurations["max_bytes"],
            max_bytes,
            "Logger should be created with configuration file.",
        )

        self.assertIsNotNone(logger, "Logger should be created with configuration file.")

    def test_regex_time_format(self):
        """Test if the date format is converted to regex without errors."""
        strftime_directive = get_date_as_regex("%Y-%m-%d %H:%M:%S")
        plain_date = get_date_as_regex("2010-11-12 12:34:56")
        self.assertEqual(
            strftime_directive,
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
            "strftime directive should be converted to regex.",
        )

        self.assertEqual(
            plain_date,
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
            "Plain date should be converted to regex.",
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
