from camara import Camara

print("ESTE ES EL CAMBIO REALIZADO")

titulo_programa = "CÁMARA FOTOGRÁFICA"
print(f"╔═{"═" * len(titulo_programa)}═╗")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"║ {titulo_programa} ║")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"╚═{"═" * len(titulo_programa)}═╝")

print("~ DATOS DE LA CÁMARA ~")
marca = input("Ingrese la marca: ")
modelo = input("Ingrese el modelo: ")
almacenamiento = int(input("Ingrese el almacenamiento (MB): "))

camara = Camara(marca, modelo, almacenamiento)

while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~ MENÚ ~")
    print("Ingrese un número:")
    print("1. Mostrar información")
    print("2. Añadir fotos")
    print("3. Borrar fotos")
    print("4. Modificar información")
    print("5. Salir")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    res = input("→ ")
    
    if res == "1":
        print("=====================================================================================")
        print("~ INFORMACIÓN ~")
        print(camara)
        print("=====================================================================================")
        print("Para volver pulse Enter")
        input("→ ")
    
    elif res == "2":
        print("-------------------------------------------------------------------------------------")
        print("~ AÑADIR FOTOS ~")
        fotos = int(input("Ingrese la cantidad de fotos (cada una pesa 5 MB): "))
        if camara.get_almacenamiento() < camara.get_ocupado() + fotos * 5 or fotos < 1:
            print("=====================================================================================")
            print("Ingrese una cantidad válida. No se aceptan números negativos ni que excedan el\nlímite de almacenamiento.")
            print("=====================================================================================")
            print("Para volver pulse Enter")
            input("→ ")
        else:
            camara + fotos
            print("=====================================================================================")
            print("Las fotos se añadieron correctamente.")
            print("=====================================================================================")
            print("Para volver pulse Enter")
            input("→ ")
    
    elif res == "3":
        print("-------------------------------------------------------------------------------------")
        print("~ BORRAR FOTOS ~")
        fotos = int(input("Ingrese la cantidad de fotos: "))
        if fotos < 1 or fotos > camara.get_fotos():
            print("=====================================================================================")
            print("Ingrese una cantidad válida. No se aceptan números negativos ni que excedan la\ncantidad de fotos almacenada.")
            print("=====================================================================================")
            print("Para volver pulse Enter")
            input("→ ")
        else:
            camara - fotos
            print("=====================================================================================")
            print("Las fotos se borraron correctamente.")
            print("=====================================================================================")
            print("Para volver pulse Enter")
            input("→ ")

    elif res == "4":
        print("-------------------------------------------------------------------------------------")
        print("~ MODIFICAR DATOS ~")
        print("Elija qué dato desea modificar:")
        print("1. Marca")
        print("2. Modelo")
        print("3. Almacenamiento")
        dato = input("→ ")
        print("-------------------------------------------------------------------------------------")
        if dato == "1":
            marca = input("Ingrese la marca: ")
            camara.set_marca(marca)
            print("=====================================================================================")
            print("Marca modificada correctamente.")
            print("=====================================================================================")
        elif dato == "2":
            modelo = input("Ingrese el modelo: ")
            camara.set_modelo(modelo)
            print("=====================================================================================")
            print("Modelo modificado correctamente.")
            print("=====================================================================================")
        elif dato == "3":
            almacenamiento = int(input("Ingrese el almacenamiento: "))
            if camara.get_ocupado() > almacenamiento:
                print("=====================================================================================")
                print("El espacio ocupado es mayor que el almacenamiento que desea utilizar, elimine\nfotos o ingrese un almacenamiento mayor.")
                print("=====================================================================================")
            else:
                camara.set_almacenamiento(almacenamiento)
                print("=====================================================================================")
                print("Almacenamiento modificado correctamente.")
                print("=====================================================================================")
        else:
            print("=====================================================================================")
            print("Debe ingresar una de las tres alternativas.")
            print("=====================================================================================")
        print("Para volver pulse Enter")
        input("→ ")

    elif res == "5":
        break