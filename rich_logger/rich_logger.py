import rich


class RichLogger:
    def __init__(self):
        pass

    def info(self, message: str):
        print(message)


if __name__ == "__main__":
    logger = RichLogger()
    logger.info("Hello World")
