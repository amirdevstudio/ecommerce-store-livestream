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

class QueryFilterTemplates:
    @staticmethod
    def _compile_as_filters(filter_: QueryFilter) -> QueryFilters:
        filters = QueryFilters()
        filters.add(filter_)
        return filters

    @classmethod
    def where_field_in_values(cls, field_: str, value: Iterable[Any], compiled_as_filters: bool = True):
        res = QueryFilter(
            field=field_,
            value=value,
            operator=QueryFilterOperators.IN
        )

        if compiled_as_filters:
            res = cls._compile_as_filters(res)

        return res

    @classmethod
    def where_id_equals_value(cls, value: int, compile_as_filters: bool = True):
        res = QueryFilter(
            field="id",
            value=value,
            operator=QueryFilterOperators.EQUALS
        )

        if compile_as_filters:
            res = cls._compile_as_filters(res)

        return res
