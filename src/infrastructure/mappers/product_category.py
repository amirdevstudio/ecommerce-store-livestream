from src.application.interfaces.mapper import AbstractEntityMapper, _DomainEntity
from src.infrastructure.database.postgresql.orm.models.product import ProductCategory as ProductCategoryOrmModel
from src.domain.models.product import ProductCategory as ProductCategoryDomainModel


class ProductCategoryOrmMapper(AbstractEntityMapper[ProductCategoryDomainModel, ProductCategoryOrmModel]):
    def domain_to_dict(self, domain_entity: ProductCategoryDomainModel) -> dict:
        return {
            'id': domain_entity.id if domain_entity.id else None,
            'name': domain_entity.name
        }

    def domain_to_orm(self, domain_entity: ProductCategoryDomainModel) -> ProductCategoryOrmModel:
        return ProductCategoryOrmModel(
            id=domain_entity.id if domain_entity.id else None,
            name=domain_entity.name
        )

    def orm_to_domain(self, orm_entity: ProductCategoryOrmModel) -> ProductCategoryDomainModel:
        return ProductCategoryDomainModel(
            id=orm_entity.id,
            name=orm_entity.name
        )
