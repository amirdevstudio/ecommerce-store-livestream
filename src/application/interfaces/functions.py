from abc import ABC, abstractmethod


class AbstractFunction(ABC):
    @abstractmethod
    def call(self, *args, **kwargs):
        ...


class AbstractFunctionExecutor(ABC):
    @abstractmethod
    def execute(self, function: AbstractFunction, *args, **kwargs):
        ...
