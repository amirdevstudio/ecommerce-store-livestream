from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.entities.abstract import AbstractEntity


@dataclass
class AbstractHttpRequestDto(ABC):
    @abstractmethod
    def to_domain_model(self) -> AbstractEntity:
        ...


@dataclass
class AbstractHttpResponseDto(ABC):

    @classmethod
    @abstractmethod
    def from_domain_model(cls, model: AbstractEntity) -> 'AbstractHttpResponseDto':
        ...
