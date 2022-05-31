from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from crear_tabla import *

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

print("Consulta 1")
codPar = session.query(Establecimiento, Parroquia).join(Parroquia).filter(Parroquia.codigo == "110553").all()

for e in codPar:
	print("%s " % (e))
        


print("Consulta 2")
provAu = session.query(Establecimiento.nombreInstitucion).join(Parroquia, Canton, Provincia).filter(Provincia.nombre == 'EL ORO').all()

for o in provAu:
	print("%s " % (o))


print("Consulta 3")
canPor = session.query(Establecimiento).join(Canton).\
        filter(Canton.nombre == "PORTOVELO").all()

for p in canPor:
	print(p)

canZam = session.query(Establecimiento).join(Canton).\
        filter(Canton.nombre == "ZAMORA").all()

print("Consulta 4")

for z in canZam:
	print(z)
