from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

print("Consulta 1")

canNum = session.query(Canton.nombre).join(Parroquia, Establecimiento).\
    filter(or_(Establecimiento.numDocentes == 0, Establecimiento.numDocentes ==
           5, Establecimiento.numDocentes == 11)).all()

for e in canNum:
    print("%s " % (e))

print("Consulta 2")

esJor = session.query(Establecimiento.nombreInstitucion).join(Parroquia).\
    filter(and_(Establecimiento.numEstudiantes >=
           21, Parroquia.nombre == "PINDAL")).all()

for e in esJor:
    print("%s " % (e))
