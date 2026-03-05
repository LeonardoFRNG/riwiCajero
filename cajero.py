saldo = 1000

operaciones = int(input("Cuantas operaciones desea realizar? "))

for i in range(operaciones):
    print("\n===Cajero Automatico===")
    print("1= Consultar Saldo")
    print("2= Retirar dinero")
    print("3= Depositar dinero")

    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        print(f"Su saldo actual es: {saldo}")

    elif opcion == 2:
        monto = float(input("Ingrese el monto a retirar: "))

        while monto < 0:
            monto = float(input("Monto invalido. ingrese nuevamente: "))
        
        if monto > saldo:
            print("Fondos insuficientes. ")
        else:
            saldo = saldo - monto
            print(f"Retiro exito. Nuevo saldo: {saldo}")

    elif opcion == 3:
        monto = float(input("Ingrese el monto a depositar: "))
        while monto < 0:
            monto = float(input("Monto inválido. Ingrese nuevamente:"))
        saldo = saldo + monto
        print("Deposito exitoso, nuevo saldo: ", saldo)
    else:
        print("Opcion invalida")
    print("Gracias por usar el cajero")
    
    
