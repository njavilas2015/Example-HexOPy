from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DiscountOutputDTO:
    id: int
    name: str
    percentage: float
    is_visible: bool
