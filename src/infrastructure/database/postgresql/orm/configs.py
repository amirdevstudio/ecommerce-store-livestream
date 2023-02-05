from contextvars import ContextVar
from datetime import datetime

from inflection import tableize
# noinspection PyProtectedMember
from peewee import (
    _ConnectionState,
    BigAutoField,
    PostgresqlDatabase,
    Model,
    DateTimeField,
)

_db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
_db_state = ContextVar("_db_state", default=_db_state_default.copy())

class _PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", _db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


database = PostgresqlDatabase(
    'ecommerce_store.dev',
    user='postgres',
    password='root'
)

database._state = _PeeweeConnectionState()


class BaseEntity(Model):
    id = BigAutoField()
    db_record_created_at = DateTimeField(default=datetime.now)
    db_record_updated_at = DateTimeField(default=datetime.now)
    db_record_deleted_at = DateTimeField(null=True)

    class Meta:
        database = database

        @staticmethod
        def table_function(model_class):
            if hasattr(model_class, "__tablename__"):
                return model_class.__tablename__
            return tableize(model_class.__name__)


BaseAssociation = BaseEntity
