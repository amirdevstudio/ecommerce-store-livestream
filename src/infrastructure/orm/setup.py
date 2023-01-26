from peewee import Database, Model


def setup_tables(database: Database, models: list[Model]) -> None:
    database.connect()
    database.create_tables(models)
    database.close()
