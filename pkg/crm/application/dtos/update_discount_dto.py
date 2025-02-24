from decimal import Decimal

from pydantic import field_validator
from pydantic.dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UpdateDiscountDTO:
    id: int
    name: str
    percentage: Decimal
    is_visible: bool

    @field_validator("name")
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return v

    @field_validator("percentage")
    def validate_percentage(cls, v: Decimal):
        if v < 0 or v > 100:
            raise ValueError("The percentage must be between 0 and 100")
        return v
