from peewee import *

db = SqliteDatabase("db_tp_final.db")


class BaseModel(Model):
    class Meta:
        database = db


class Historiaclinica(BaseModel):
    nro_historia_clinica = AutoField(unique=True)
    nombre_mascota = CharField()
    edad = IntegerField()
    color = CharField()
    especie = CharField()
    raza = CharField()
    sexo = CharField()
    nombre_duenio = CharField()
    mail = CharField()
    telefono = IntegerField()
    direccion = TextField()
    ciudad = CharField()


db.connect()
db.create_tables([Historiaclinica])
