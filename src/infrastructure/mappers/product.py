from amir_dev_studio.dependency_injection import get_service

from src.infrastructure.database.postgresql.orm.models.product import Product as ProductOrmModel
from src.domain.entities.product import Product as ProductDomainModel
from src.infrastructure.mappers.abstract import AbstractEntityMapper
from src.infrastructure.mappers.product_category import ProductCategoryMapper
from src.infrastructure.mappers.product_tag import ProductTagMapper


class ProductMapper(AbstractEntityMapper[ProductDomainModel, ProductOrmModel]):
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
            price=domain_entity.price
        )

    def orm_to_domain(
            self,
            orm_entity: ProductOrmModel,
            should_map_recursively: bool = True
    ) -> ProductDomainModel:
        categories = []
        tags = []

        if should_map_recursively:
            tag_mapper = get_service(ProductTagMapper)
            for tag_relation in orm_entity.tag_relations:
                tag = tag_relation.tag
                tags.append(tag_mapper.orm_to_domain(tag))

            category_mapper = get_service(ProductCategoryMapper)
            for category_relation in orm_entity.category_relations:
                category = category_relation.category
                categories.append(category_mapper.orm_to_domain(category))

        return ProductDomainModel(
            id=orm_entity.id,
            name=orm_entity.name,
            description=orm_entity.description,
            price=orm_entity.price,
            tags=tags,
            categories=categories
        )
