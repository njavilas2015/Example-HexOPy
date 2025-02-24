from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Discount:
    id: int
    name: str
    percentage: float
    is_visible: bool