from src.domain.entities.product import ProductTag as ProductTagDomainModel
from src.infrastructure.database.postgresql.orm.models.product import ProductTag as ProductTagOrmModel
from src.infrastructure.mappers.abstract import AbstractEntityMapper


class ProductTagMapper(AbstractEntityMapper[ProductTagDomainModel, ProductTagOrmModel]):
    def domain_to_dict(self, domain_entity: ProductTagDomainModel) -> dict:
        return {
            'id': domain_entity.id if domain_entity.id else None,
            'name': domain_entity.name
        }

    def domain_to_orm(self, domain_entity: ProductTagDomainModel):
        return ProductTagOrmModel(
            id=domain_entity.id if domain_entity.id else None,
            name=domain_entity.name,
        )

    def orm_to_domain(self, orm_entity: ProductTagOrmModel):
        return ProductTagDomainModel(
            id=orm_entity.id,
            name=orm_entity.name,
        )
