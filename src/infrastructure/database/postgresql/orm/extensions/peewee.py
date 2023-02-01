import peewee

from src.application.pagination import PaginationOptions
from src.application.query_filters import QueryFilters, QueryFilterOperators, QueryFilter
from src.application.sorting import SortingOptions, SortingOption, SortingDirections


class PeeweeSelectQueryExtension:
    def __init__(self, query: peewee.ModelSelect):
        self.query = query

    def _get_column(self, column_name: str) -> peewee.Field | None:
        return getattr(self.query.model, column_name, None)

    def _apply_sort(self, sort: SortingOption):
        column = self._get_column(sort.field)

        if column is None:
            return

        if sort.direction is SortingDirections.ASCENDING:
            self.query = self.query.order_by(column.asc())

        elif sort.direction is SortingDirections.DESCENDING:
            self.query = self.query.order_by(column.desc())

    def _apply_filter(self, filter_: QueryFilter):
        column = self._get_column(filter_.field)

        if column is None:
            return

        operator = filter_.operator
        value = filter_.value

        if operator == QueryFilterOperators.EQUALS:
            self.query = self.query.where(column == value)
        elif operator == QueryFilterOperators.NOT_EQUALS:
            self.query = self.query.where(column != value)
        elif operator == QueryFilterOperators.GREATER_THAN:
            self.query = self.query.where(column > value)
        elif operator == QueryFilterOperators.GREATER_THAN_OR_EQUAL:
            self.query = self.query.where(column >= value)
        elif operator == QueryFilterOperators.LESS_THAN:
            self.query = self.query.where(column < value)
        elif operator == QueryFilterOperators.LESS_THAN_OR_EQUAL:
            self.query = self.query.where(column <= value)
        elif operator == QueryFilterOperators.CONTAINS:
            self.query = self.query.where(column.contains(value))
        elif operator == QueryFilterOperators.NOT_CONTAINS:
            self.query = self.query.where(~column.contains(value))
        elif operator == QueryFilterOperators.STARTS_WITH:
            self.query = self.query.where(column.startswith(value))
        elif operator == QueryFilterOperators.NOT_STARTS_WITH:
            self.query = self.query.where(~column.startswith(value))
        elif operator == QueryFilterOperators.ENDS_WITH:
            self.query = self.query.where(column.endswith(value))
        elif operator == QueryFilterOperators.NOT_ENDS_WITH:
            self.query = self.query.where(~column.endswith(value))
        elif operator == QueryFilterOperators.IN:
            self.query = self.query.where(column.in_(value))
        elif operator == QueryFilterOperators.NOT_IN:
            self.query = self.query.where(~column.in_(value))

    def apply_filters(self, filters: QueryFilters):
        for filter_ in filters.filters.values():
            self._apply_filter(filter_)

    def apply_pagination(self, pagination_options: PaginationOptions):
        self.query = self.query.paginate(pagination_options.page, pagination_options.per_page)

    def apply_sorting(self, sorting_options: SortingOptions):
        for option in sorting_options.options.values():
            self._apply_sort(option)
