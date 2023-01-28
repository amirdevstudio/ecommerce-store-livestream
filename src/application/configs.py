from amir_dev_studio.dependency_injection import add_transient_service

from src.application.functions.create_product import CreateProduct
from src.application.functions.get_product import GetProduct
from src.application.functions.get_products import GetProducts


def configure_dependencies():
    add_transient_service(CreateProduct)
    add_transient_service(GetProduct)
    add_transient_service(GetProducts)
