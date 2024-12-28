<sub><sub> [Text to ASCII Art Generator](https://patorjk.com/software/taag/#p=display&c=bash&f=Rectangles&t=RichLogger)
</sub></sub>

```
   _____ _     _   __
  | __  |_|___| |_|  |   ___ ___ ___ ___ ___
  |    -| |  _|   |  |__| . | . | . | -_|  _|
  |__|__|_|___|_|_|_____|___|_  |_  |___|_|
                            |___|___|
```

---

# RichLogger

A simple Logger for Python which includes rich formatting for console prints.

# Idea

The idea is to have this logging class to do the heavy lifting to initialize the python logging module and support printing to the console.
If logging to a file is not necessary the library can be used in the same way, by simply printing to the console or do nothing.

# Usage

To use the RichLogger library, follow these steps:

1. Install the library using pip:

   ```bash
   pip install rich-logger
   ```

2. Import the library in your Python script:

   ```python
   from rich_logger import RichLogger
   ```

3. Initialize the logger:

   ```python
   logger = RichLogger(name="my_logger", level="DEBUG")
   ```

4. Use the logger to log messages:
   ```python
   logger.debug("This is a debug message")
   logger.info("This is an info message")
   logger.warning("This is a warning message")
   logger.error("This is an error message")
   logger.critical("This is a critical message")
   ```

The logger will handle the formatting and output of the messages to the console.

If you want to log only to a file use:

```python
logger = RichLogger(logging_to_file=True, logging_to_console=False)
```

You can also combine both and have a console and file logging by setting the variables `logging_to_file` and `logging_to_console` accordingly.

# Tests

Tests run locally via:

```bash
coverage run -m unittest discover tests/
```

Visualized with:

```bash
coverage report -m
```

Resulting in:

| Name                                      | Stmts   | Miss  | Cover    | Missing |
| ----------------------------------------- | ------- | ----- | -------- | ------- |
| rich_logger\_\_init\_\_.py                | 0       | 0     | 100%     |
| rich_logger\console_logger_highlighter.py | 12      | 0     | 100%     |
| rich_logger\defaults.py                   | 3       | 0     | 100%     |
| rich_logger\rich_logger.py                | 47      | 0     | 100%     |
| rich_logger\utils.py                      | 16      | 0     | 100%     |
| tests\test_rich_logger.py                 | 36      | 0     | 100%     |
| **TOTAL**                                 | **114** | **0** | **100%** |

Tested python versions:

- 3.11.11
- 3.12.8
- 3.13.1

# License

The License is MIT, for further information see `License` file
