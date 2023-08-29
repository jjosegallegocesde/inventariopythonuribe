#MENU DE OPCIONES
#1. Ingresar producto bodega
#2. Verificar los productos en bodega
#3. Buscar un producto en la bodega
#4. Editar un producto en la bodega
#5. Retirar un producto bodega
#6. SALIR

#producto:nombre,codigo,descripcion,foto,precio,cantidadEnBodega,fechaEntradaBodega

opcion=0
print("TIENDA EL GANGAZO")
print("************")
print("1. Ingresar producto bodega")
print("2. Verificar los productos en bodega")
print("3. Buscar un producto en la bodega")
print("4. Editar un producto en la bodega")
print("5. Retirar un producto bodega")
print("6. SALIR")
print("************")

productos = []


while(opcion != 6):
    producto = {}
    opcion=int(input("Digita la opcion deseada: "))
    if opcion==1:
        producto["nombre"] = input("Digita el nombre del producto: ")
        producto["codigo"] = int(input("Digita el codigo del producto: "))
        producto["descripcion"] = input("Digita la descripción del producto: ")
        producto["foto"] = input("Digita la URL de la foto: ")
        producto["precio"] = float(input("Digita el precio del producto: "))
        producto["stock"] = int(input("Digite el stock del producto "))
        producto["fechaEntradaBodega"] = input("Digita la fecha de entrada: ")
        productos.append(producto)  
    elif opcion==2:
        for productoSeleccionado in productos:
            print(f"codigo = {productoSeleccionado['codigo']}")
            print(f"nombre = {productoSeleccionado['nombre']}")
            print(f"descripcion = {productoSeleccionado['descripcion']}")
            print(f"foto = {productoSeleccionado['foto']}")
            print(f"cantidad en bodega = {productoSeleccionado['stock']}")
            print(f"Fecha de entrada = {productoSeleccionado['fechaEntradaBodega']}\n")
            
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("Opcion invalida, vuelva a intentarlo")
        
    