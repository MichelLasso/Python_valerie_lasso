def menuOpcion():
    print("\nMENU DE PYTIMES")
    print("1. Subscripciones anuales")
    print("2. Saldo de su cuenta")
    print("3. Subscripcines de regalo")
    print("4. Historial de subscripciones anuales ")
    print("5. fin")

print("\nPYTIMES :)")
print("\n¡HOLA!, bienvenido a PYtimes ")

historial_subs_anuales_regalo =set()
historial_subs_anuales = set() # Almacena los años de suscripción anuales
costoSubs=50000

nameUsuario=input("Por favor, ingrese su nombre: ")
cuentaUsuario=int(input("ingrese el valor de su cuenta"))

menuOpcion()

opcionUsuario=int(input("ingresa el número de la opcion del menú que deseas "))

bool=True
while bool==True:
    if opcionUsuario==1:
        
        
        print("\nOh, deseas comprar una subscripción anual\nBienvenido a subscripciones anuales")
        sub=True
        while sub==True:

                print("\nuna subscripcion anual tiene un precio de: ",costoSubs)
                
                siNo=int(input("Deseas comprarla?\n1.si\n2.no\n°"))
                
                if siNo==1:
                    
                    if cuentaUsuario >=costoSubs:
                            
                        cuentaUsuario=cuentaUsuario-costoSubs
                            
                        print("te queda un saldo de: ",cuentaUsuario)
                        
                        siNo2=input("Ingrese el año de su compra: ")       
                        
                        historial_subs_anuales.add(siNo2 ) # Agrega el año a la lista de suscripciones anuales
                                                             
                        print("Tu suscripción ha sido registrada con éxito!!!")
                        print("\nen el mensaje siguiente ingresa el número 2 para cerrar la compra")
                    else:
                            
                        print("No tienes saldo suficiente\nTienes un saldo  de: ",cuentaUsuario)

                if siNo==2:  
                 sub=False


        menuOpcion()

        opcionUsuario=int(input("ingresa el número de la opcion del menú que deseas "))


    if opcionUsuario==2:
        print("\nSALDO DE SU CUENTA :)")
        print("su saldo es de : ",cuentaUsuario)

        menuOpcion()

        opcionUsuario=int(input("ingresa el número de la opcion del menú que deseas "))

    
    if opcionUsuario==3:

            sub2=True

            while sub2==True:

                print("\nSUSCRIPCIONES DE REGALO")
                
                print("\nuna subscripcion anual tiene un precio de: ",costoSubs)
                
                siNo3=int(input("Deseas comprarla?\n1.si\n2.no\n°"))

                if siNo3==1:
                    
                    if cuentaUsuario >=costoSubs:
                            
                        cuentaUsuario=cuentaUsuario-costoSubs

                        nameRegalo=input("ingresa el nombre de la persona que obtendra este regalo: ")
                        
                        print("te queda un saldo de: ",cuentaUsuario)
                        
                        siNo4=input("Ingrese el año de su compra: ")


                        historial_subs_anuales_regalo.add(siNo4 ) # Agrega el año a la lista de suscripciones anuales
                                
                        print("Tu suscripción de regalo ha sido registrada con éxito!!!")                   
                        print("\nen el mensaje siguiente ingresa el número 2 para cerrar la compra")
                    else:
                            
                        print("No tienes saldo suficiente\nTienes un saldo  de: ",cuentaUsuario)

                if siNo3==2:  
                 sub2=False
            menuOpcion()

            opcionUsuario=int(input("ingresa el número de la opcion del menú que deseas "))  

    if opcionUsuario==4:

        print("\nHISTORIAL DE SUBSCRIPCIONES ANUALES")
        print(nameUsuario)
        print(historial_subs_anuales)

        print("\nHISTORIAL DE SUBSCRIPCION DE REGALO")
        print(nameRegalo)
        print(historial_subs_anuales_regalo)

        menuOpcion()

        opcionUsuario=int(input("ingresa el número de la opcion del menú que deseas ")) 

    if opcionUsuario==5:
      print("Gracias por usar PYtimes\nBAYBAY\n:)")
      bool=False 