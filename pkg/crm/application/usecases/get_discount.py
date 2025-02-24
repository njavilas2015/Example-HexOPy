from pkg.crm.application.dtos.discount_output_dto import DiscountOutputDTO
from pkg.crm.infrastructure.transformers.discount_transformer import DiscountTransformer

from pkg.crm.infrastructure.persistence.repositories.discount_repository import (
    DiscountRepository,
)


class GetDiscount:
    transformer: DiscountTransformer
    repository: DiscountRepository

    def __init__(self, repository: DiscountRepository):
        self.transformer = DiscountTransformer()
        self.repository = repository

    async def execute(self, id: int) -> DiscountOutputDTO | None:
        return await self.repository.get_by_id(id=id)
