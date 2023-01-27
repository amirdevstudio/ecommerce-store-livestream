from amir_dev_studio.dependency_injection import get_service
from fastapi import APIRouter

from src.application.functions.get_products import GetProducts
from src.application.interfaces.functions import AbstractFunctionExecutor

router = APIRouter(prefix='/products', tags=['Products'])

@router.get('')
def get_products():
    executor = get_service(AbstractFunctionExecutor)
    function = get_service(GetProducts)

    return executor.execute(function)


@router.get('/{product_id}')
def get_product(product_id: str):
    return {
        'product': 'product1'
    }


@router.patch('/{product_id}')
def patch_product(product_id: str):
    return {
        'product': 'product1'
    }


@router.post('')
def create_product():
    return {
        'product': 'product1'
    }


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
