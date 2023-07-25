import pandas as pd
from data.platos import platosPopulares
from data.proveedores import Proveedores
from data.reservas import Reservas
from data.creartabla import crearTabla

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos,"tablaplatospopulares")

tablaProveedor=pd.DataFrame(Proveedores)
print(tablaProveedor)
crearTabla(tablaProveedor,"Proveedores")

tablaReservas=pd.DataFrame(Reservas)
print(tablaReservas)
crearTabla(tablaReservas,"tablaReservas")