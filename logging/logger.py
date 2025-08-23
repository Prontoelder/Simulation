class Logger:
    """Class for logging simulation events."""

    def __init__(self) -> None:
        self._messages: list[str] = []

    def log(self, message: str) -> None:
        """Add a message to the log."""
        self._messages.append(message)

    def get_messages_and_clear(self) -> list[str]:
        """Get all messages and clear the log."""
        messages = self._messages.copy()
        self._messages = []
        return messages


game_logger = Logger()
