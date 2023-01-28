from typing import Optional, List

from amir_dev_studio.dependency_injection import get_service
from fastapi import APIRouter, Depends

from src.application.functions.create_product import CreateProduct
from src.application.functions.get_products import GetProducts
from src.application.interfaces.functions import AbstractFunctionExecutor
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters, QueryFilter, QueryFilterOperators
from src.application.sorting import SortingOptions, SortingOption, SortingDirections
from src.web.api.v1.dependencies import get_pagination_options
from src.web.dtos.product import ProductHttpPostRequestDto, ProductHttpPostResponseDto

router = APIRouter(prefix='/products', tags=['Products'])


def get_sorting_options(
        name_sorting_direction: Optional[SortingDirections] = None,
        price_sorting_direction: Optional[SortingDirections] = None,
):
    return SortingOptions.from_tuples([
        ('name', name_sorting_direction),
        ('price', price_sorting_direction)
    ])


def get_query_filters(
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
        filters: QueryFilters = Depends(get_query_filters),
        sorting_options: SortingOptions = Depends(get_sorting_options),
        pagination_options: PaginationOptions = Depends(get_pagination_options)
) -> PaginatedResults:
    executor = get_service(AbstractFunctionExecutor)
    function = get_service(GetProducts)

    return executor.execute(
        function,
        filters=filters,
        sorting_options=sorting_options,
        pagination_options=pagination_options
    )


@router.get('/{product_id}')
def get_product_by_id(product_id: str):
    return {
        'product': 'product1'
    }


@router.patch('/{product_id}')
def patch_product(product_id: str):
    return {
        'product': 'product1'
    }


@router.post('', status_code=201)
def create_product(request_dto: ProductHttpPostRequestDto) -> ProductHttpPostResponseDto:
    executor = get_service(AbstractFunctionExecutor)
    function = get_service(CreateProduct)

    product = request_dto.to_domain_model()
    product = executor.execute(function, product=product)
    return ProductHttpPostResponseDto.from_domain_model(product)


@router.put('/{product_id}')
def update_product(product_id: str):
    return {
        'product': 'product1'
    }


@router.delete('/{product_id}')
def delete_product(product_id: str, is_deactivating: bool = True):
    return {
        'product': 'product1'
    }
