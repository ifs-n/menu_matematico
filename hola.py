import os
os.system("cls")

flag = True

while flag:
    print("------Menú matemático")
    print("1. Contar del 1 al N")
    print("2. Mostrar números pares")
    print("3. Tabla de multiplicar")
    print("4. Salir")
    
    opcion = int(input("Ingrese una opcion:\n"))
    
    if opcion == 1:
        num = int(input("Ingrese un número:\n"))
        for x in range(1, num + 1):
            print(f"{0 + x}")
        
    elif opcion == 2:
        num = int(input("Ingrese un número:\n"))
        for x in range(1, num +1 ):
            if x % 2 == 0:
                print(f"{x}")
                
    elif opcion == 3:
        num = int(input("Ingrese un número:\n"))
        for x in range(1, 11):
            multi = num * x
            print(f"{multi}")
    elif opcion == 4:
        flag = False
    else:
        print("Opción inválida.")