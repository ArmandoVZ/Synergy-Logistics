import pandas as pd
from collections import Counter

database = pd.read_csv( 'C:/Users/arman/Desktop/PROYECTO-02-VEGA-ARMANDO/synergy_logistics_database.csv')

routes = [i +"-"+ j for i, j in zip(list(database["origin"]), list(database["destination"]))] #Unimos las listas "Origen" y "Destino"
database['route'] = routes

routes_dicc = list(dict.fromkeys(routes)) # Creamos una lista con todas las rutas.
routes_counter = Counter(routes) #Obtenemos una cuenta con todas las veces que se han utilizad las rutas.
routes_sorted,route_profit = [],[]

for route in routes_dicc: #Creamos una lista "nested"
    nested=[]
    routes_sorted.append(nested)
    for k in range(1):
        nested.append(route)
        nested.append(routes_counter[route])

def Sort(routes_sorted): #Ordenamos las rutas
    routes_sorted.sort(key = lambda x: x[1], reverse=True)
    return routes_sorted
routes_sorted = Sort(routes_sorted) # 

print("\nRUTAS MAS USADAS \n")
tempsum = 0
for i in range(0,10):
    print( F'ROUTE: {routes_sorted[i][0]}\t TIMES USED: {routes_sorted[i][1]}')
    tempsum += routes_sorted[i][1]
    if i >= 9:
        print(f'\nRESUMEN DE LAS 10 RUTAS MAS USADAS: {"{:,.0f}".format(tempsum)}\t PORCENTAJE DE LAS EXPORTACIONES: {"{:,.2f}%".format(100*tempsum/len(routes))}')

routes_transport_profit = list(zip(list(database["route"]), list(database["transport_mode"]),list(database["total_value"])))

tempsum = 0    
for route in routes_dicc:
    for i in range(0,len(list(routes_transport_profit))):
        if route == routes_transport_profit[i][0]:
            tempsum += routes_transport_profit[i][-1]
    nested=[]
    route_profit.append(nested)
    for k in range(1):
        nested.append(route)
        nested.append(tempsum)
    tempsum = 0

def Sort(route_profit): #Ordenamos las rutas
    route_profit.sort(key = lambda x: x[-1], reverse=True)
    return route_profit
route_profit = Sort(route_profit) 

print("\nRUTAS CON MAYORES GANANCIAS \n")
tempsum = 0
for i in range(0,10):
    print( F'ROUTE: {route_profit[i][0]}\t PROFITS: {"${:,.0f}".format(route_profit[i][-1])}')
    tempsum += route_profit[i][-1]
    if i >= 9:
        print(f'\n RESUMEN DE LAS 10 RUTAS CON MAYORES GANANCIAS: {"${:,.0f}".format(tempsum)}\t PORCENTAJE DE GANANCIAS: {"{:,.2f}%".format(100*tempsum/database["total_value"].sum())}')

#------------------------------TRANSPORT----------------------------#
transport_dicc = list(dict.fromkeys(database["transport_mode"])) #Generamos una lista con todos los medios de transporte
transport_profit = []

tempsum = 0
for transport in transport_dicc:
    for i in range(0,len(list(routes_transport_profit))):
        if transport == routes_transport_profit[i][1]:
            tempsum += routes_transport_profit[i][-1]
    nested=[]
    transport_profit.append(nested)

transport_profit = []

tempsum = 0
for transport in transport_dicc:
    for i in range(0,len(list(routes_transport_profit))):
        if transport == routes_transport_profit[i][1]:
            tempsum += routes_transport_profit[i][-1]
    nested=[]
    transport_profit.append(nested)
    for k in range(1):
        nested.append(transport)
        nested.append(tempsum)
    tempsum = 0

def Sort(transport_profit): #Ordenamos la lista de medios de trasporte
    transport_profit.sort(key = lambda x: x[-1], reverse=True)
    return transport_profit
transport_profit = Sort(transport_profit) 

print("\nMEDIOS DE TRASPORTE CON MAYORES GANANCIAS \n")
tempsum = 0
for i in range(0,4):
    print( F'TRANSPORT: {transport_profit[i][0]}\t PROFITS: {"${:,.0f}".format(transport_profit[i][-1])}')
    if i >= 3:
        print(f'\nMEDIOS DE TRANSPORTE CON MAYORES GANANCIAS: {"${:,.0f}".format(transport_profit[0][-1])}\t PORCENTAJE DE GANANCIAS: {"{:,.2f}%".format(100*transport_profit[0][-1]/database["total_value"].sum())}')

#----------------------------------EXPORTS-----------------------------------#

origin_dicc = list(dict.fromkeys(database["origin"])) #Creamos una lista con todos los origenes
origin_dest_profit = list(zip(list(database["origin"]), list(database["destination"]),list(database["total_value"])))

origin_profit=[]

tempsum = 0
for origin in origin_dicc:
    for i in range(0,len(list(origin_dest_profit))):
        if origin == origin_dest_profit[i][0]:
            tempsum += origin_dest_profit[i][-1]
    nested=[]
    origin_profit.append(nested)
    for k in range(1):
        nested.append(origin)
        nested.append(tempsum)
    tempsum = 0

def Sort(origin_profit): #Ordenando las rutas
    origin_profit.sort(key = lambda x: x[-1], reverse=True)
    return origin_profit
origin_profit = Sort(origin_profit) 

print("\nEXPORTACIONES CON MAYORES GANANCIAS\n")
tempsum = 0
for i in range(0,8):
    print( F'ORIGIN: {origin_profit[i][0]}\t PROFITS: {"${:,.0f}".format(origin_profit[i][-1])}')
    tempsum += origin_profit[i][-1]
    if i >= 7:
        print(f'\nRESUMEN DE GANANCIAS GENERADAS POR LAS EXPORTACIONES CON MEJORES RENDIMIENTOS: {"${:,.0f}".format(tempsum)}\t PORCENTAJE DE LAS GANANCIAS TOTALES: {"{:,.2f}%".format(100*tempsum/database["total_value"].sum())}')

#----------------------------------IMPORTS-----------------------------------#
destination_dicc = list(dict.fromkeys(database["destination"])) #Obtenemos una lista con todos los "destinos" con los cuales, calcularemos las importaciones
destination_profit=[]

tempsum = 0
for destination in destination_dicc:
    for i in range(0,len(list(origin_dest_profit))):
        if destination == origin_dest_profit[i][1]:
            tempsum += origin_dest_profit[i][-1]
    nested=[]
    destination_profit.append(nested)
    for k in range(1):
        nested.append(destination)
        nested.append(tempsum)
    tempsum = 0

def Sort(destination_profit): #Ordenamos la lista
    destination_profit.sort(key = lambda x: x[-1], reverse=True)
    return destination_profit
destination_profit = Sort(destination_profit)

print("\nIMPORTACIONES CON MEJOR RENDIMIENTO\n")
tempsum = 0
for i in range(0,13):
    print( F'DESTINATION: {destination_profit[i][0]}\t PROFITS: {"${:,.0f}".format(destination_profit[i][-1])}')
    tempsum += destination_profit[i][-1]
    if i >= 12:
        print(f'\nRESUMEN DE LAS IMPORTACIONES CON MEJOR RENDIMIENTO: {"${:,.0f}".format(tempsum)}\t PORCENTAJE DE LAS GANANCIAS TOTALES: {"{:,.2f}%".format(100*tempsum/sum(database["total_value"]))}')