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
        },
    ):
        self.keywords = keywords_n_styles.keys()
        self.styles = keywords_n_styles

    def highlight(self, text):
        for keyword in self.keywords:
            text.highlight_regex(rf"\b{keyword}\b", self.styles[keyword])
