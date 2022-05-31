from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_  # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

print("Consulta 1")

esCod = session.query(Establecimiento.nombreInstitucion).\
    filter(Establecimiento.numDocentes > 100).order_by(
        Establecimiento.numEstudiantes).all()

for c in esCod:
    print("%s " % (c))

print("Consulta 2")

esCod = session.query(Establecimiento.nombreInstitucion).\
    filter(Establecimiento.numDocentes > 100).order_by(
        Establecimiento.numDocentes).all()

for c in esCod:
    print("%s " % (c))
