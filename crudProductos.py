productos = []

flag = True

while flag:
    print("MENU PRINCIPAL")
    print("-----------------------")
    print("1- Ingresar producto")
    print("2- Ver productos")
    print("3- Eliminar producto")
    print("4- Actualizar producto")
    print("5- Salir del menu")

    dato = int(input("Elegir un numero dado del menu: "))

    if dato == 1:
        respuesta = input("Ingresar un producto para añadirlo: ")
        productos.append(respuesta)
        print(f"El producto que se añadio fue: {respuesta}")

    elif dato ==2:
        print(f"Listado de productos: {productos}")

    elif dato ==3:
        eliminar = input("Ingresar un producto a eliminar: ")
        productos.remove(eliminar)
        print(f"Se elimino producto {eliminar}")

    elif dato ==4:
        actualizar = input("Ingresar un producto a actualizar: ")
        producto_actualizar = productos.index(actualizar)
        modificar = input("Ingresar la modificacion del producto: ")
        for prod in productos:
            if prod == actualizar:
                productos[producto_actualizar] = modificar
                print(f"El producto actualizado es: {modificar}")

    elif dato ==5:
        print("Fin del programa")
        flag = False 
        
    else:
        print("Error")