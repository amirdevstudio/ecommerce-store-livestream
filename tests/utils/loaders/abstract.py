from abc import abstractmethod, ABC

from tests.utils.factories.orm.factory import OrmFactory


class IDataLoader(ABC):
    @abstractmethod
    def load(self, *args, **kwargs):
        ...


class AbstractDataLoader(IDataLoader, ABC):
    def __init__(self, factory: OrmFactory):
        self.factory = factory
        self.loaded_orm_entities = []

    def load(self, __count: int = 5):
        entities = self.factory.create_many(__count)
        for entity in entities:
            entity.save()
            self.loaded_orm_entities.append(entity)
