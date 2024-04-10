import random 
print("BIENVENIDO AL JUEGO")
print("El objetivo es acertar en la menor cantidad de intentos. ")
conti = "si"

while conti.lower() == "si":
 # numero secreto aleatorio entre 1 y 100
 nuSecreto = random.randint(1,100)

 nIntentos = 0
 adivinado = False

 # Bucle de todo el proceso del juego 
 while not adivinado:
    num = input("Ingresa un número entre 1 y 100: ")
    
    # si el usuario ingreso algo fuera de un número 
    if not num.isdigit():
        print("")
        print("ingresa un número valido.")
        continue
    
    num = int(num)
    
    # numero fuera de 100 o menor de 1
    if num < 1 or num > 100:
        print("")
        print("El número debe estar entre  1 a 100.")
        continue
    nIntentos += 1

    # si es alto o bajo 
    if num < nuSecreto:
        print("")
        print("El número es mayor. ¡Intenta nuevamente!")
    elif num > nuSecreto:
        print("")
        print("El número es menor. ¡Intenta nuevamente!")
    else:
        print("")
        print(f"¡WAO! Adivinaste el número en {nIntentos} intentos :) ")
        adivinado = True

    print(f"Número de intentos : {nIntentos}")
    print("")

 conti = input("¿Desea continuar? (si/no): ")
 if conti.lower() == "no":
    print("Hasta luego")

#desarrollado por Valerie Lasso C.I 1.093.296.678