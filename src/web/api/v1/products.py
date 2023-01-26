from fastapi import APIRouter

router = APIRouter(prefix='/products', tags=['products'])

@router.get('')
def get_products():
    return {
        'products':
            [
                'product1',
                'product2'
            ]
    }


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
