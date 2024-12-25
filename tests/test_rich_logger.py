import unittest

from rich_logger.rich_logger import RichLogger


class TestRichLoggerImport(unittest.TestCase):
    def test_import_works(self):
        """Test if the RichLogger class can be imported without errors."""
        try:
            logger = RichLogger()
            self.assertIsInstance(
                logger, RichLogger, "RichLogger should be an instance of its class."
            )
        except Exception as e:
            self.fail(f"Importing RichLogger failed with error: {e}")


if __name__ == "__main__":
    unittest.main()
