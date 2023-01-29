from dataclasses import dataclass
from typing import Optional

from src.domain.models.abstract import AbstractModel


@dataclass
class BaseModel(AbstractModel):
    id: Optional[int]
