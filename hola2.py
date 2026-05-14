import os
os.system("cls")

flag = True
acum_deposito = 0
acum_cantidad = 0

try:
    while flag:

        print("========= BANCO ESTAO =========")
        print("1. Mostrar cuotas de ahorro")
        print("2. Simular depósito acumulado")
        print("3. Tabla de crédito")
        print("4. Contar clientes atendidos")
        print("5. Salir")

        opcion = int(input("Ingrese una opción:\n"))

        if opcion == 1:
            ahorro = int(input("Ingrese ahorro mensual:\n"))
            while ahorro <= 0:
                ahorro = int(input("El ahorro no puede ser negativo, ingrese otra vez:\n"))
            meses = int(input("Ingrese la cantidad de meses:\n"))
            while meses <= 0:
                meses = int(input("La cantidad de meses no puede ser menor a 0, ingrese otra vez:\n"))

            for x in range(1, meses + 1):
                ahorro_mes = 0 + ahorro
                ahorro_final = ahorro_mes * x
                print (f"Mes {x}: ${ahorro_final}")

        elif opcion == 2:
            banderita = True
            while banderita:
                deposito = int(input("Ingrese el depósito:\n"))
                while deposito < 0:
                    deposito = int(input("El deposito no puede ser negativo:\n"))
                acum_deposito = acum_deposito + deposito
                acum_cantidad = acum_cantidad + 1
                if deposito == 0:
                    banderita = False
            print(f"Total acumulado: {acum_deposito}")
            print(f"Cantidad de depósitos: {acum_cantidad - 1}")

        elif opcion == 3:
            credito = int(input("Ingrese el monto del crédito: \n"))
            while credito <= 0:
                credito = int(input("El monto del crédito debe ser mayor a 0, ingrese el monto:\n"))
            for x in range(1, 13):
                credito_mes = credito * x
                print(f"{credito} x {x}: ${credito_mes}")
        elif opcion == 4:
            clientes = int(input("Ingrese la cantidad de clientes: \n"))
            while clientes <= 0:
                clientes = int(input("La cantidad de clientes debe ser mayor a 0:\n"))
            for x in range (1, clientes +1 ):
                print(f"Cliente atendido N°{x}")
        elif opcion == 5:
            flag = False
        else:
            print("Opción no válida.")
except:
    print("Una de las opciones ingresadas no corresponde al tipo de dato solicitado.")