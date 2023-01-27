from datetime import datetime

from inflection import tableize
from peewee import PostgresqlDatabase, Model, IntegerField, DateTimeField


database = PostgresqlDatabase(
    'ecommerce_store.dev',
    user='postgres',
    password='root'
)


class BaseModel(Model):
    id = IntegerField(primary_key=True)
    db_record_created_at = DateTimeField(default=datetime.now)
    db_record_updated_at = DateTimeField(default=datetime.now)
    db_record_deleted_at = DateTimeField(null=True)

    class Meta:
        database = database

        @staticmethod
        def table_function(model_class):
            return tableize(model_class.__name__)


BaseAssociation = BaseModel
