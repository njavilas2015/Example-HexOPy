from pydantic.dataclasses import dataclass
from pydantic import field_validator


@dataclass(frozen=True, slots=True)
class DeleteDiscountDTO:
    id: int

    @field_validator("id")
    def validate_id(cls, v: int):
        if v <= 0:
            raise ValueError("ID must be a positive integer")
        return v
