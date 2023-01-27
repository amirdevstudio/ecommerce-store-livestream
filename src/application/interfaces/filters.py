from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any


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
class AbstractQueryFilter:
    field: str
    value: Any
    operator: QueryFilterOperators

    Operators = QueryFilterOperators


@dataclass
class AbstractQueryFilters:
    filters: Dict[str, AbstractQueryFilter]
