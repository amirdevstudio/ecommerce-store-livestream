from dataclasses import dataclass

from src.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    email: str
    password: str


@dataclass
class Role(BaseEntity):
    name: str
    permissions: list['Permission']


@dataclass
class Permission(BaseEntity):
    resource: str
    action: str
