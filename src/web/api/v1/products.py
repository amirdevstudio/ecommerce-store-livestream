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
