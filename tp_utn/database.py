# Importa la clase SqliteDatabase del módulo peewee
from peewee import *

# Importa la clase Mensajes del módulo mensajes
from mensajes import Mensajes

# Crea una instancia de SqliteDatabase con el nombre del archivo de base de datos
db = SqliteDatabase("db_tp_final.db")
# Crea una instancia de la clase Mensajes
mensaje = Mensajes()


# Define la clase BaseModel que actuará como clase base para todos los modelos y especifica la base de datos
class BaseModel(Model):
    """
    # Clase base para todos los modelos. Establece la conexión a la base de datos.
    """

    class Meta:
        database = db


# Define el modelo Historiaclinica que hereda de BaseModel
class Historiaclinica(BaseModel):
    # Modelo de datos para representar la información de las historias clínicas.
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


try:
    # Intenta establecer la conexión a la base de datos y crear las tablas
    db.connect()
    print("Conexión a la base de datos establecida correctamente.")
    db.create_tables([Historiaclinica])
    print("tablas creadas")
except OperationalError as e:
    # Si hay un error arroja un print con el mismo.
    print(f"Error al conectar a la base de datos: {e}")
finally:
    # Cierra la conexión a la base de datos en cualquier caso
    db.close()
    print("Conexión a la base de datos cerrada correctamente.")
