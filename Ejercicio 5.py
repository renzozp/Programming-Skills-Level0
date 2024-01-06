#EJERCICIO 5
#USER: renzozp15
"""
5. Develop a finance management application with the following features:
* 		The user records their total income.
* 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 		The user can list their expenses within the categories and get the total for each category.
* 		The user can obtain the total of their expenses.
* 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
* 		If the user spends more than they earn, the system will display advice to improve the user's financial health.

"""

#Ingreso de datos
sueldo=0
medico=0
house= 0
leisure=0
saving=0
education=0
while True :
    print("Aplicación de finanzas personales")
    lista = ["Ingreso de sueldo" , "Ingreso de Medical expense", " Ingreso de Household expense" , "Ingreso de leisure" , " Ingreso de saving", "Ingreso de education", "Listar gastos"]
    lista_dinero =[medico,house, leisure,saving, education]
    lista_gastos =["medico: ","house: ", "leisure: ","saving: ", "education: "]
    for i, opcion in enumerate (lista):
        print(f"{i+1}.{opcion}")

    opcion_elegida= int( input(" Ingrese el numero de la opción que desea realizar: "))

    if opcion_elegida ==1:
        sueldo= int(input("Ingrese su sueldo: "))
    elif opcion_elegida ==2:
        medico= int(input("Ingrese su gasto medico: "))
    elif opcion_elegida ==3:
        house= int(input("Ingrese su gasto de casa: "))
    elif opcion_elegida ==4:
        leisure= int(input("Ingrese su gasto de ocio: "))
    elif opcion_elegida ==5:
        saving= int(input("Ingrese sus ahorro: "))
    elif opcion_elegida ==6:
        education= int(input("Ingrese su gasto de educación: "))
    elif opcion_elegida ==7:
        print( " LISTA DE GASTOS INGRESADOS" )
        print( "    Medical expense: ", medico)
        print( "    Household expense: ", house)
        print( "    Leisure expense: ", leisure)
        print( "    Saving expense: ", saving)
        print( "    Education expense: ", education)

        
    while True :
                otra= input(f" desea realizar otra operación(s/n); ")
                if otra.lower() == "s":
                    break
                else:
                    print("gracias por usar el sistema")
                    gasto_total= medico + house + leisure + saving + education
                    gasto_maximo= max(medico,house,leisure,saving,education)
                    if sueldo == gasto_total:
                        print("DEBE REDUCIR SUS GASTOS EN LA CATEGORIA ", gasto_maximo)
                    elif sueldo > gasto_total:
                        print(" FELICIDADES POR AHORRAR DINERO")
                    elif sueldo < gasto_total:
                        print("DEBES MEJORAR TUS FINANZAS PERSONALES")
                    exit()


             
