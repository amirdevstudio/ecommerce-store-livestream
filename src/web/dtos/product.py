from dataclasses import dataclass

from src.web.dtos.abstract import AbstractHttpRequestDto, AbstractHttpResponseDto
from src.domain.models.product import Product
from src.web.dtos.product_category import ProductCategoryHttpResponseDto, ProductCategoryHttpRequestDto
from src.web.dtos.product_tag import ProductTagHttpResponseDto, ProductTagHttpRequestDto


@dataclass
class ProductHttpResponseDto(AbstractHttpResponseDto):
    id: int
    name: str
    price: float
    description: str
    description_excerpt: str
    tags: list[ProductTagHttpResponseDto]
    categories: list[ProductCategoryHttpResponseDto]

    @classmethod
    def from_domain_model(cls, product: Product) -> 'ProductHttpResponseDto':
        if len(product.description) > 200:
            excerpt = product.description[:197] + '...'
        else:
            excerpt = product.description

        tag_dtos = []
        for tag in product.tags:
            tag_dto = ProductTagHttpResponseDto.from_domain_model(tag)
            tag_dtos.append(tag_dto)

        category_dtos = []
        for category in product.categories:
            category_dto = ProductCategoryHttpResponseDto.from_domain_model(category)
            category_dtos.append(category_dto)

        return cls(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            description_excerpt=excerpt,
            tags=tag_dtos,
            categories=category_dtos
        )


@dataclass
class ProductHttpRequestDto(AbstractHttpRequestDto):
    name: str
    price: float
    description: str
    tags: list[ProductTagHttpRequestDto]
    categories: list[ProductCategoryHttpRequestDto]

    def to_domain_model(self) -> Product:
        tags = [tag_dto.to_domain_model() for tag_dto in self.tags]
        categories = [category_dto.to_domain_model() for category_dto in self.categories]

        return Product(
            id=None,
            name=self.name,
            price=self.price,
            description=self.description,
            tags=tags,
            categories=categories
        )


@dataclass
class ProductHttpRequestDtoWithId:
    id: int
    name: str
    price: float
    description: str
    tags: list[ProductTagHttpRequestDto]
    categories: list[ProductCategoryHttpRequestDto]

    def to_domain_model(self) -> Product:
        tags = [tag_dto.to_domain_model() for tag_dto in self.tags]
        categories = [category_dto.to_domain_model() for category_dto in self.categories]

        return Product(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            tags=tags,
            categories=categories
        )
