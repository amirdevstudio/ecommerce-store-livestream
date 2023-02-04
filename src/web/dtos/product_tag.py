from dataclasses import dataclass

from src.domain.entities.product import ProductTag
from src.web.dtos.abstract import AbstractHttpResponseDto, AbstractHttpRequestDto


@dataclass
class ProductTagHttpResponseDto(AbstractHttpResponseDto):
    id: int
    name: str

    @classmethod
    def from_domain_model(cls, model: ProductTag) -> 'ProductTagHttpResponseDto':
        return cls(
            id=model.id,
            name=model.name,
        )


@dataclass
class ProductTagHttpRequestDto(AbstractHttpRequestDto):
    name: str

    def to_domain_model(self) -> ProductTag:
        return ProductTag(
            id=None,
            name=self.name,
        )
