opcion =0
while opcion !=6:   
    print("MENU DE EJERCICIOS")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Salir")
    print("------------------")
    opcion = int(input("Elija una opcion: "))
    match opcion:   
        case 1:
            #PD: Este lo hice yo
            Rango =0
            inicio =0
            Rango = int(input("Ingrese el rango del conteo: "))

            while Rango > inicio:
                if Rango %2 !=0:
                    print(Rango)
                Rango = Rango-1
        case 2:
            rango = int(input("Ingrese el rango del conteo: "))
            inicio = 0
            numeros_impares = []

            while rango > inicio:
                if rango % 2 != 0:
                    numeros_impares.append(rango)
                rango -= 1 
            print(", ".join(map(str, numeros_impares)))
            
        case 3:
            filas =6
            columnas = 6
            matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
                    
        case 4:
            num_lineas = int(input("ingrese la cantidadd de filas: "))
            for i in range(num_lineas):
                print(" " * i , "*" * (num_lineas * 2 - i * 2 - 1))
        case 5:
            num_lineas = int(input("ingrese la cantidadd de filas: "))
            
            for i in range(num_lineas):
                print(" " * (num_lineas - i - 1) , "*" * ( 2 * i + 1))
                
            for i in range(num_lineas):
                print(" " * i , "*" * (num_lineas * 2 - i * 2 - 1))
    
