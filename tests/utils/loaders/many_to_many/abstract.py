from abc import ABC

from tests.utils.loaders.abstract import IDataLoader


class AbstractManyToManyDataLoader(IDataLoader, ABC):
    def __init__(self):
        self.loaded_entities = []
