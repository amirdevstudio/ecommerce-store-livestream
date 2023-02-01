from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Iterable


class QueryFilterOperators(Enum):
    EQUALS = "eq"
    NOT_EQUALS = "neq"
    GREATER_THAN = "gt"
    GREATER_THAN_OR_EQUAL = "gte"
    LESS_THAN = "lt"
    LESS_THAN_OR_EQUAL = "lte"
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    STARTS_WITH = "starts_with"
    NOT_STARTS_WITH = "not_starts_with"
    ENDS_WITH = "ends_with"
    NOT_ENDS_WITH = "not_ends_with"
    IN = "in"
    NOT_IN = "not_in"


@dataclass
class QueryFilter:
    field: str
    value: Any
    operator: QueryFilterOperators

@dataclass
class QueryFilters:
    filters: Dict[str, QueryFilter] = field(default_factory=dict, init=False)

    def add(self, filter_: QueryFilter):
        self.filters[filter_.field] = filter_

    def merge(self, query_filters: 'QueryFilters'):
        self.filters.update(query_filters.filters)

    @classmethod
    def from_tuples(cls, tuples: list[tuple[str, Any, QueryFilterOperators]]):
        filters = cls()
        for field_, value, operator in tuples:
            if not value:
                continue
            filters.add(
                QueryFilter(
                    field=field_,
                    value=value,
                    operator=operator
                )
            )
        return filters

class QueryFilterRecipes:
    @staticmethod
    def where_field_in_values(field_: str, value: Iterable[Any]):
        return QueryFilters.from_tuples([(field_, value, QueryFilterOperators.IN)])

    @staticmethod
    def where_id_equals_value(value: int):
        return QueryFilters.from_tuples([("id", value, QueryFilterOperators.EQUALS)])
