from dataclasses import dataclass

from src.domain.models.product import ProductCategory
from src.web.dtos.abstract import AbstractHttpResponseDto


@dataclass
class ProductCategoryHttpResponseDto(AbstractHttpResponseDto):
    id: int
    name: str

    @classmethod
    def from_domain_model(cls, category: ProductCategory) -> 'ProductCategoryHttpResponseDto':
        return cls(
            id=category.id,
            name=category.name
        )


@dataclass
class ProductCategoryHttpRequestDto:
    name: str

    def to_domain_model(self) -> ProductCategory:
        return ProductCategory(
            id=None,
            name=self.name
        )
