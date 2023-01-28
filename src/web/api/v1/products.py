from typing import Optional

from amir_dev_studio.dependency_injection import get_service
from fastapi import APIRouter, Depends, Body

from src.application.functions.create_product import CreateProduct
from src.application.functions.delete_product_hard import HardDeleteProduct
from src.application.functions.delete_product_soft import SoftDeleteProduct
from src.application.functions.get_products import GetProducts
from src.application.functions.update_product_price import UpdateProductPrice
from src.application.interfaces.functions import AbstractFunctionExecutor
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters, QueryFilterOperators
from src.application.sorting import SortingOptions, SortingDirections
from src.web.api.v1.dependencies import get_pagination_options
from src.web.dtos.product import ProductHttpRequestDto, ProductHttpResponseDto

router = APIRouter(prefix='/products', tags=['Products'])


def _get_sorting_options(
        name_sorting_direction: Optional[SortingDirections] = None,
        price_sorting_direction: Optional[SortingDirections] = None,
):
    return SortingOptions.from_tuples([
        ('name', name_sorting_direction),
        ('price', price_sorting_direction)
    ])


def _get_query_filters(
        name: Optional[str] = None,
        price: Optional[str] = None,
        name_operator: Optional[QueryFilterOperators] = QueryFilterOperators.EQUALS,
        price_operator: Optional[QueryFilterOperators] = QueryFilterOperators.EQUALS
):
    return QueryFilters.from_tuples([
        ('name', name, name_operator),
        ('price', price, price_operator)
    ])


@router.get('', response_model=None)
def get_products(
        filters: QueryFilters = Depends(_get_query_filters),
        sorting_options: SortingOptions = Depends(_get_sorting_options),
        pagination_options: PaginationOptions = Depends(get_pagination_options),
        executor: AbstractFunctionExecutor = Depends(lambda: get_service(AbstractFunctionExecutor)),
        function: GetProducts = Depends(lambda: get_service(GetProducts))
) -> PaginatedResults:
    return executor.execute(
        function,
        filters=filters,
        sorting_options=sorting_options,
        pagination_options=pagination_options
    )


@router.get('/{product_id}')
def get_product(
        product_id: int,
        executor: AbstractFunctionExecutor = Depends(lambda: get_service(AbstractFunctionExecutor)),
        function: GetProducts = Depends(lambda: get_service(GetProducts))
) -> ProductHttpResponseDto:
    product = executor.execute(function, product_id=product_id)
    return ProductHttpResponseDto.from_domain_model(product)


@router.patch('/{product_id}/price')
def patch_product_price(
        product_id: str,
        price: int = Body(embed=True),
        executor: AbstractFunctionExecutor = Depends(lambda: get_service(AbstractFunctionExecutor)),
        function: GetProducts = Depends(lambda: get_service(UpdateProductPrice))
) -> ProductHttpResponseDto:
    product = executor.execute(function, product_id=product_id, price=price)
    return ProductHttpResponseDto.from_domain_model(product)


@router.post('', status_code=201)
def create_product(
        request_dto: ProductHttpRequestDto,
        executor: AbstractFunctionExecutor = Depends(lambda: get_service(AbstractFunctionExecutor)),
        function: CreateProduct = Depends(lambda: get_service(CreateProduct))
) -> ProductHttpResponseDto:
    product = request_dto.to_domain_model()
    product = executor.execute(function, product=product)
    return ProductHttpResponseDto.from_domain_model(product)


@router.put('/{product_id}')
def update_product(
        product_id: str,
        product: ProductHttpRequestDto,
        executor: AbstractFunctionExecutor = Depends(lambda: get_service(AbstractFunctionExecutor)),
        function: GetProducts = Depends(lambda: get_service(UpdateProductPrice))
) -> ProductHttpResponseDto:
    product = product.to_domain_model()
    product = executor.execute(function, product_id=product_id, product=product)
    return ProductHttpResponseDto.from_domain_model(product)


@router.delete('/{product_id}', status_code=204)
def delete_product(
        product_id: str,
        is_soft_delete: bool = True,
        executor: AbstractFunctionExecutor = Depends(lambda: get_service(AbstractFunctionExecutor)),
        hard_delete_function: GetProducts = Depends(lambda: get_service(HardDeleteProduct)),
        soft_delete_function: GetProducts = Depends(lambda: get_service(SoftDeleteProduct))
) -> None:
    if is_soft_delete:
        executor.execute(soft_delete_function, product_id=product_id)
    else:
        executor.execute(hard_delete_function, product_id=product_id)
