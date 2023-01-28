from dataclasses import dataclass

from src.web.dtos.abstract import HttpRequestBodyDto, HttpResponseBodyDto
from src.domain.models.product import Product


@dataclass
class ProductHttpGetResponseDto(HttpResponseBodyDto):
    name: str
    price: float
    description: str
    description_excerpt: str

    @classmethod
    def from_domain_model(cls, product: Product):
        if len(product.description) > 200:
            excerpt = product.description[:197] + '...'
        else:
            excerpt = product.description

        return cls(
            name=product.name,
            price=product.price,
            description=product.description,
            description_excerpt=excerpt
        )


@dataclass
class ProductHttpPostRequestDto(HttpRequestBodyDto):
    name: str
    price: float
    description: str

    def to_domain_model(self):
        return Product(
            id=None,
            name=self.name,
            price=self.price,
            description=self.description
        )


@dataclass
class ProductHttpPostResponseDto(HttpResponseBodyDto):
    name: str
    price: float
    description: str

    @classmethod
    def from_domain_model(cls, product: Product) -> 'ProductHttpPostResponseDto':
        return cls(
            name=product.name,
            price=product.price,
            description=product.description
        )
