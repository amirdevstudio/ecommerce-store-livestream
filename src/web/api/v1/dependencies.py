from typing import Optional

from src.application.pagination import PaginationOptions


def get_pagination_options(
        page: Optional[int] = 1,
        per_page: Optional[int] = 10
):
    return PaginationOptions(
        page=page,
        per_page=per_page
    )
