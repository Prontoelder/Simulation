from collections import defaultdict

from config import config


class Logger:
    """Class for logging simulation events."""

    def __init__(self) -> None:
        self._messages: list[str] = []

    def log(self, message: str) -> None:
        """Add a message to the log."""
        self._messages.append(message)

    def _get_messages_and_clear(self) -> list[str]:
        """Get all messages and clear the log."""
        messages = self._messages.copy()
        self._messages.clear()
        return messages

    def print_game_logs(self) -> None:
        """Group and prints all accumulated events messages."""
        grouped = defaultdict(list)
        logs = self._get_messages_and_clear()

        for log in logs:
            parts = log.split(":", 1)
            if len(parts) == 2:
                action_type, rest = parts
                grouped[action_type].append(rest.strip())
            else:
                grouped["OTHER"].append(log)

        for action_type, messages in grouped.items():
            action_type_print = f"{action_type}: "
            for i in range(0, len(messages), config.max_logs_per_line):
                chunk = messages[i : i + config.max_logs_per_line]
                print(action_type_print + ", ".join(chunk))
        print()


game_logger = Logger()
