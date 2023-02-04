from enum import Enum


class AutoName(Enum):
    def _generate_next_value_(name, _start, _count, _last_values):  # type: ignore
        return name
