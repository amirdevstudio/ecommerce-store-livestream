from abc import ABC, abstractmethod
from typing import Generic, TypeVar

ReturnType = TypeVar("ReturnType")


class AbstractFunction(ABC, Generic[ReturnType]):
    @abstractmethod
    def call(self, *args, **kwargs) -> ReturnType:
        ...


class AbstractFunctionExecutor(ABC):
    @abstractmethod
    def execute(self, function: AbstractFunction[ReturnType], *args, **kwargs) -> ReturnType:
        ...
