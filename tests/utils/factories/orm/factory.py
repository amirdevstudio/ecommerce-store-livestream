from src.application.interfaces.mapper import IEntityMapper
from tests.utils.factories.abstract import IFactory, AbstractFactory


class OrmFactory(IFactory):
    def __init__(
            self,
            factory: AbstractFactory,
            mapper: IEntityMapper,
    ):
        self.factory = factory
        self.mapper = mapper

    def create_many(self, __count: int = 5, *args, **kwargs):
        entities = [self.create(*args, **kwargs) for _ in range(__count)]

        for i, entity in enumerate(entities):
            entities[i] = self.mapper.orm_to_domain(entity)

        return entities

    def create(self, *args, **kwargs):
        entity = self.factory.create(*args, **kwargs)
        entity = self.mapper.domain_to_orm(entity)
        return entity
