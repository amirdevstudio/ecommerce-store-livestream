from dataclasses import dataclass

from src.web.dtos.abstract import HttpRequestBodyDto, HttpResponseBodyDto
from src.domain.models.product import Product


@dataclass
class ProductHttpResponseDto(HttpResponseBodyDto):
    id: int
    name: str
    price: float
    description: str
    description_excerpt: str

    @classmethod
    def from_domain_model(cls, product: Product) -> 'ProductHttpResponseDto':
        if len(product.description) > 200:
            excerpt = product.description[:197] + '...'
        else:
            excerpt = product.description

        return cls(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            description_excerpt=excerpt
        )


@dataclass
class ProductHttpRequestDto(HttpRequestBodyDto):
    name: str
    price: float
    description: str

    def to_domain_model(self) -> Product:
        return Product(
            id=None,
            name=self.name,
            price=self.price,
            description=self.description
        )


@dataclass
class ProductHttpRequestDtoWithId:
    id: int
    name: str
    price: float
    description: str

    def to_domain_model(self) -> Product:
        return Product(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description
        )
