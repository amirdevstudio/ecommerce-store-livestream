from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.models.abstract import AbstractModel


@dataclass
class AbstractHttpRequestDto(ABC):
    @abstractmethod
    def to_domain_model(self) -> AbstractModel:
        ...


@dataclass
class AbstractHttpResponseDto(ABC):

    @classmethod
    @abstractmethod
    def from_domain_model(cls, model: AbstractModel) -> 'AbstractHttpResponseDto':
        ...
