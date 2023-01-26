from datetime import datetime

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
