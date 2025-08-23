class Coordinate:
    """Represents coordinate point on the game map."""
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Coordinate)
            and self.x == other.x
            and self.y == other.y
        )

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
