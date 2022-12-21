from peewee import (CharField, IntegerField, Model,
ForeignKeyField, DateTimeField)
from .dataBase import data_base

class BaseModel(Model):
    Id = IntegerField(unique=True, primary_key=True)
    class Meta:
        database = data_base


class Group(BaseModel):
    group_base = IntegerField()


class User(BaseModel):
    first_name = CharField()
    last_name = CharField()
    telegram_id = IntegerField(unique=True)
    group_id = ForeignKeyField(Group, backref="user")
    group_num = IntegerField()
    

class Lesson(BaseModel):
    name = CharField()
    group_id = ForeignKeyField(Group, backref="lesson")
    adress = CharField(default = "")
    date = DateTimeField(null=True)


class Recording(BaseModel):
    user_id = ForeignKeyField(User, backref="recording", on_delete="CASCADE")
    lesson_id = ForeignKeyField(Lesson, backref="recording", on_delete="CASCADE")


class Admins(BaseModel):
    user_id = ForeignKeyField(User.Id, backref="admins")