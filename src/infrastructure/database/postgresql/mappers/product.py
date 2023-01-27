from src.infrastructure.database.postgresql.mappers.base import AbstractOrmMapper
from src.infrastructure.database.postgresql.orm.models import Product as ProductOrmModel
from src.domain.models.product import Product as ProductDomainModel


class ProductOrmMapper(AbstractOrmMapper[ProductDomainModel, ProductOrmModel]):
    def domain_to_orm(self, domain_entity: ProductDomainModel) -> ProductOrmModel:
        return ProductOrmModel()

    def orm_to_domain(self, orm_entity: ProductOrmModel) -> ProductDomainModel:
        pass
