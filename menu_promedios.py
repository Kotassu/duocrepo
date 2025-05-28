#promedios
while True:
    opc = int(input("¿Que desea hacer?\n1. Agregar nota\n2. Calcular promedio\n3. Salir\n"))
    
    if opc == 1:
        cant_notas = int(input("¿Cuantas notas desea agregar?\n"))
        list_notas = []
        notas = int(input("Ingrese la nota: "))
        list_notas.append(notas)
    elif opc == 2:
        suma = 0
        for nota in list_notas:
            suma = nota + suma
        promedio = suma / len(list_notas)
        print(f"El promedio es: {promedio}")
    elif opc == 3:
        print("Saliendo del programa...")
        break