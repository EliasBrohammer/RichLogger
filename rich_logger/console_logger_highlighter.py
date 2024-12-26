import re

from rich.highlighter import Highlighter


class ConsoleLoggerHighlighter(Highlighter):
    """
    Highlights specific keywords with custom styles.
    """

    def __init__(
        self,
        keywords_n_styles: dict = {
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold red",
            "TIME": "cyan",
        },
        regex_time_format: str = r"\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
    ):
        self.keywords = keywords_n_styles.keys()
        self.styles = keywords_n_styles
        self.regex_time_format = regex_time_format

    def highlight(self, text):
        # Highlight keywords
        for keyword in self.keywords:
            if keyword != "TIME":
                text.highlight_regex(rf"\b{keyword}\b", self.styles[keyword])

        # Highlight time
        text.highlight_regex(self.regex_time_format, self.styles["TIME"])
