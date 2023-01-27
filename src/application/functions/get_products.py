from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.filters import AbstractQueryFilters
from src.application.interfaces.pagination import AbstractPaginationOptions
from src.application.interfaces.repositories import AbstractProductRepository
from src.application.interfaces.functions import AbstractFunction
from src.application.interfaces.sorting import AbstractSortingOptions
from src.infrastructure.utils import get_default_logger


class GetProducts(AbstractFunction):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)
        self.logger = get_default_logger(__name__)

    def call(
            self,
            filters: AbstractQueryFilters,
            sorting_options: AbstractSortingOptions,
            pagination_options: AbstractPaginationOptions,
    ):
        return self.repository.get(
            filters=filters,
            sorting_options=sorting_options,
            pagination_options=pagination_options
        )
