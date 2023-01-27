from amir_dev_studio.dependency_injection import add_transient_service

from src.application.functions.get_products import GetProducts


def configure_dependencies():
    add_transient_service(GetProducts)
