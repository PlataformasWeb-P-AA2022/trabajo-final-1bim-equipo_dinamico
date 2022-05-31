from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

print("Consulta 1")
esJor = session.query(Parroquia.nombre).join(Establecimiento).filter(Establecimiento.jornada == "Matutina y Vespertina").all()

for e in esJor:
	print("%s " % (e))


print("Consulta 2")

esNum = session.query(Canton.nombre).join(Parroquia,Establecimiento).filter(or_(Establecimiento.numEstudiantes == 448, 
Establecimiento.numEstudiantes == 450, 
Establecimiento.numEstudiantes == 451, 
Establecimiento.numEstudiantes == 454, 
Establecimiento.numEstudiantes == 458, 
Establecimiento.numEstudiantes == 459)).all()

for j in esNum:
	print("%s " % (j))