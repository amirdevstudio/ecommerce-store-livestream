from abc import ABC, abstractmethod
from typing import Generic, TypeVar

ReturnType = TypeVar("ReturnType")


class AbstractUseCase(ABC, Generic[ReturnType]):
    @abstractmethod
    def call(self, *args, **kwargs) -> ReturnType:
        ...


class AbstractUseCaseExecutor(ABC):
    @abstractmethod
    def execute(self, function: AbstractUseCase[ReturnType], *args, **kwargs) -> ReturnType:
        ...
