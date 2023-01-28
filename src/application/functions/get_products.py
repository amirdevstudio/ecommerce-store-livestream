from amir_dev_studio.dependency_injection import get_service

from src.application.pagination import PaginationOptions
from src.application.query_filters import QueryFilters
from src.application.interfaces.repositories import AbstractProductRepository
from src.application.interfaces.functions import AbstractFunction
from src.application.sorting import SortingOptions
from src.infrastructure.utils import get_default_logger


class GetProducts(AbstractFunction):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)
        self.logger = get_default_logger(__name__)

    def call(
            self,
            filters: QueryFilters,
            sorting_options: SortingOptions,
            pagination_options: PaginationOptions,
    ):
        return self.repository.get(
            filters=filters,
            sorting_options=sorting_options,
            pagination_options=pagination_options
        )
