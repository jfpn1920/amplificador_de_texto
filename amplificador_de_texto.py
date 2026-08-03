import random
ids = []
titulos = []
textos_originales = []
textos_ampliados = []
veces = []
fechas = []
estados = []
observaciones = []
#------------------------------------------#
#--|menu_principal_amplificador_de_texto|--#
#------------------------------------------#
while True:
    print("menu principal amplificador de texto")
    print("1) crear texto")
    print("2) editar texto")
    print("3) eliminar texto")
    print("4) buscar texto")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|crear_texto|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_texto = 1
        else:
            id_texto = ids[-1] + 1
        titulo = input("título: ")
        texto_original = input("texto original: ")
        cantidad = int(input("veces que desea amplificar el texto: "))
        fecha = input("fecha: ")
        estado = input("estado (procesado o pendiente): ")
        observacion = input("observación: ")
        texto_ampliado = ""
        for i in range(cantidad):
            texto_ampliado += texto_original + "\n"
        ids.append(id_texto)
        titulos.append(titulo)
        textos_originales.append(texto_original)
        textos_ampliados.append(texto_ampliado)
        veces.append(cantidad)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("texto registrado correctamente.")
        print("id:", id_texto)
    #------------------#
    #--|editar_texto|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar texto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos_originales[i]} | {veces[i]} veces | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos_originales[posicion]} | {veces[posicion]} veces | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                textos_originales[posicion] = input("nuevo texto original: ")
                veces[posicion] = int(input("número de veces a amplificar: "))
                fechas[posicion] = input("nueva fecha: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                texto_ampliado = ""
                for i in range(veces[posicion]):
                    texto_ampliado += textos_originales[posicion] + "\n"
                textos_ampliados[posicion] = texto_ampliado
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_texto|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar texto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos_originales[i]} | {veces[i]} veces | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos_originales[posicion]} | {veces[posicion]} veces | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    textos_originales.pop(posicion)
                    textos_ampliados.pop(posicion)
                    veces.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_texto|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar texto")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("título:", titulos[posicion])
                print("texto original:")
                print(textos_originales[posicion])
                print("texto ampliado:")
                print(textos_ampliados[posicion])
                print("veces:", veces[posicion])
                print("fecha:", fechas[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            procesados = 0
            pendientes = 0
            total_ampliaciones = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos_originales[i]} | {veces[i]} veces | {fechas[i]} | {estados[i]}")
                total_ampliaciones += veces[i]
                if estados[i].lower() == "procesado":
                    procesados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
            print("estadísticas amplificador de texto")
            print("cantidad de textos:", len(ids))
            print("textos procesados:", procesados)
            print("textos pendientes:", pendientes)
            print("total de ampliaciones realizadas:", total_ampliaciones)
            posicion = random.randint(0, len(ids) - 1)
            print("texto seleccionado")
            print("texto original:")
            print(textos_originales[posicion])
            print("texto ampliado:")
            print(textos_ampliados[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el amplificador de texto.")
        break
    else:
        print("opción no válida.")