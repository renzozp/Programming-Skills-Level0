# Primer ejercicio
# USER: renzozp15
"""
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.   
"""
#Definir usuario y password
usuario= "juancito"
password= "12345"
intentos= 3
balance= 2000
#Acceso a plataforma


while intentos > 0:

    usuario_ingresado= input("Ingrese su usuario: ")
    password_ingresado= input("Ingrese su password: ")
    if usuario_ingresado == usuario:
        acceso= 1
        break
    else:
        print ("Acceso incorrecto")
        intentos= intentos-1
        print("Vuelva a ingresar sus credenciales")

else :
    print("Sistema bloqueado")

while True :
    if acceso ==1 and intentos >0 :     
        print("Tiene las siguientes opciones para realizar:")
        print("1. Deposito")
        print("2. Retiro")
        print("3. Ver")
        print("4. Transferir")

        operacion_elegida = int(input( "Ingrese su opción: "))

        if operacion_elegida == 1:
           deposito= int( input("ingrese monto a depositar: "))
           balance= balance + deposito
           print("su saldo actual es: ", balance)
        elif operacion_elegida == 2:
            retiro= int(input(" ingrese saldo a retirar: "))
            balance= balance - retiro
            print("su saldo actual es: ", balance)
        elif operacion_elegida == 3:
            print("su saldo actual es: ", balance)
        elif operacion_elegida == 4:
            transferir= int(input("indique monto a transferir: "))
            persona= input("indique DNI de cuenta a transferir: ")
            balance= balance - transferir
            print("su saldo actual es: ", balance)
        else:
            print("opción incorrecta")
            
        while True :
            otra= input(" desea realizar otra operación(s/n); ")
            if otra.lower() == "s":
                break
            else:
                print("gracias por usar el sistema")
                exit()
            





    
