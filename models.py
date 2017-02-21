from connectdatabase import ConnectDatabase
from peewee import *


class Story(Model):
    title = CharField()
    text = CharField()
    criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()


    class Meta:
        database = ConnectDatabase.db