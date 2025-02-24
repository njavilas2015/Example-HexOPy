from typing import List
from pkg.crm.application.dtos.discount_output_dto import DiscountOutputDTO
from pkg.crm.domain.entities.discount_entity import Discount


class DiscountTransformer:
    @staticmethod
    def transform_discount_to_output(item: Discount) -> DiscountOutputDTO:
        return DiscountOutputDTO(
            id_discount=item.id,
            name=item.name,
            percentage=float(item.percentage),
            is_visible=item.is_visible,
        )

    @staticmethod
    def transform_discounts_to_outputs(
        items: List[Discount],
    ) -> List[DiscountOutputDTO]:
        return [
            DiscountTransformer.transform_discount_to_output(discount)
            for discount in items
        ]
