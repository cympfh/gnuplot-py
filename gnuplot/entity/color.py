from typing import NamedTuple


class RGB(NamedTuple):

    color: str

    def __str__(self) -> str:
        return f"rgb \"{self.color}\""
