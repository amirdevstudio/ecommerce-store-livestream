import logging

from src.application.interfaces.functions import AbstractFunction, AbstractFunctionExecutor
from src.infrastructure.utils import get_default_logger


class FunctionExecutor(AbstractFunctionExecutor):
    def __init__(self, logger: logging.Logger = None):
        self._logger = logger or get_default_logger(__name__)

    @classmethod
    def _format_exception(cls, e: Exception):
        return f"Exception occurred while calling function: {e.__class__.__name__}: {e}"

    def execute(self, function: AbstractFunction, *args, **kwargs):
        try:
            return function.call(*args, **kwargs)
        except Exception as e:
            self._logger.error(self._format_exception(e))
            raise e
