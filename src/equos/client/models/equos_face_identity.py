from enum import Enum


class EquosFaceIdentity(str, Enum):
    TOMMY = "tommy"

    def __str__(self) -> str:
        return str(self.value)
