from dataclasses import dataclass
from fastapi import APIRouter, FastAPI

from pkg.crm.infrastructure.adapters.adapter_discounts_http import (
    HttpDiscountAdapter,
    DiscountAdapter,
)

from pkg.crm.domain.services.discount_service import (
    DiscountService,
)


@dataclass(frozen=True, slots=True)
class ConfigHttpAdapter:
    Http: FastAPI
    discountService: DiscountService


class NewHttpAdapter:

    def __init__(self, config: ConfigHttpAdapter):

        discountAdapter: HttpDiscountAdapter = HttpDiscountAdapter(
            DiscountAdapter(discountService=config.discountService)
        )

        router: APIRouter = APIRouter(prefix="/crm", tags=["crm"])

        router.add_api_route(
            path="/discounts/{id}",
            methods=["GET"],
            endpoint=discountAdapter.get,
        )

        router.add_api_route(
            path="/discounts",
            methods=["GET"],
            endpoint=discountAdapter.get_all,
        )

        router.add_api_route(
            path="/discounts",
            methods=["POST"],
            endpoint=discountAdapter.create,
        )

        router.add_api_route(
            path="/discounts/{id}",
            methods=["PUT"],
            endpoint=discountAdapter.update,
        )

        router.add_api_route(
            path="/discounts/{id}",
            methods=["DELETE"],
            endpoint=discountAdapter.delete,
        )

        config.Http.include_router(router)