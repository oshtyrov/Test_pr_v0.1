from peewee import PostgresqlDatabase, Model, PrimaryKeyField, CharField, IntegerField, FloatField
from .config import host, user, password, db_name

db = PostgresqlDatabase(host=host,
                        user=user,
                        password=password,
                        database=db_name)


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db


class Country(BaseModel):
    title = CharField(100)
    region = CharField(50)
    population = IntegerField()
    p_of_world = FloatField()
    date = CharField(50)
    source = CharField(50)

    class Meta:
        db_table = 'countries'
