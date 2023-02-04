from abc import ABC, abstractmethod


class IFactory(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...

    @abstractmethod
    def create_many(self, *args, **kwargs):
        ...


class AbstractFactory(IFactory, ABC):
    def __init__(self, load_dependencies: bool = True):
        self.load_dependencies = load_dependencies

    def create_many(self, __count: int = 5, *args, **kwargs):
        return [self.create(*args, **kwargs) for _ in range(__count)]
