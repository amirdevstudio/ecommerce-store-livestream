from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.pagination import AbstractPaginationOptions
from src.application.interfaces.repositories import AbstractProductRepository
from src.application.interfaces.functions import AbstractFunction
from src.infrastructure.utils import get_default_logger


class GetProducts(AbstractFunction):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)
        self.logger = get_default_logger(__name__)

    def call(
            self,
            filters: dict = None,
            pagination_options: AbstractPaginationOptions = None,
    ):
        return self.repository.get(
            filters=filters,
            pagination_options=pagination_options
        )
