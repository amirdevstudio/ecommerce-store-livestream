from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class SortingDirections(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


@dataclass
class SortingOption:
    field: str
    direction: SortingDirections


@dataclass
class SortingOptions:
    options: Dict[str, SortingOption] = field(default_factory=dict, init=False)

    def add(self, option: SortingOption):
        self.options[option.field] = option

    @classmethod
    def from_tuples(cls, tuples: list[tuple[str, SortingDirections]]):
        options = cls()
        for sorting_field, sorting_direction in tuples:
            if sorting_direction:
                options.add(
                    SortingOption(
                        field=sorting_field,
                        direction=sorting_direction
                    )
                )
        return options
