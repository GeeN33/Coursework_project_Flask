from peewee import *

db = SqliteDatabase('Sqlite_db')

class BaseModel(Model):
    class Meta:
        database = db

class Employee(BaseModel):
    class Meta:
        db_table = 'employee'
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    phone = CharField(max_length=50)


#db.create_tables([Employee])