productoTerminadoUno={
    'referencia':5087,
    'marca':"americanino",
    'descripcion':"chompa de acampar",
    'color':"naranja",
    'costoUnitario':100000,
    'disponibleBodega':True,
    'costoVenta':850000,
    'puntosVenta':['cc mayorca','terminal norte','puerta del norte','centro de la moda']
}

productoTerminadoDos={
    'referencia':5088,
    'marca':"americanino",
    'descripcion':"Camiseta Polo",
    'color':"Azul oscuro",
    'costoUnitario':30000,
    'disponibleBodega':True,
    'costoVenta':150000,
    'puntosVenta':['cc mayorca','terminal norte','puerta del norte','centro de la moda']
}

#CREANDO UNA LISTA DE DICCIONARIOS
productos=[productoTerminadoUno,productoTerminadoDos]

#Recorriendo una LISTA con ciclo FOR
'''for contador in range(1,10,2):
    print(contador)'''

for producto in productos:
    for puntoVenta in producto["puntosVenta"]:
        print(puntoVenta)
   