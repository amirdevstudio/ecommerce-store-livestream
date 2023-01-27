from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class SortingDirection(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


@dataclass
class AbstractSortingOption(ABC):
    field: str
    direction: SortingDirection


@dataclass
class AbstractSortingOptions(ABC):
    options: Dict[str, AbstractSortingOption]
