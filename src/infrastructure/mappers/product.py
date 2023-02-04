from src.application.interfaces.mapper import IEntityMapper, _OrmEntity, _DomainEntity
from src.infrastructure.database.postgresql.orm.models.product import Product as ProductOrmModel
from src.domain.entities.product import Product as ProductDomainModel


class ProductMapper(IEntityMapper[ProductDomainModel, ProductOrmModel]):
    def domain_to_dict(self, domain_entity: ProductDomainModel) -> dict:
        return {
            'id': domain_entity.id if domain_entity.id else None,
            'name': domain_entity.name,
            'description': domain_entity.description,
            'price': domain_entity.price
        }

    def domain_to_orm(self, domain_entity: ProductDomainModel) -> ProductOrmModel:
        return ProductOrmModel(
            id=domain_entity.id if domain_entity.id else None,
            name=domain_entity.name,
            description=domain_entity.description,
            price=domain_entity.price,
        )

    def orm_to_domain(self, orm_entity: ProductOrmModel) -> ProductDomainModel:
        return ProductDomainModel(
            id=orm_entity.id,
            name=orm_entity.name,
            description=orm_entity.description,
            price=orm_entity.price,
        )
