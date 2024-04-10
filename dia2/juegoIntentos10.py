import random

# Explicación del juego
print("Bienvenido ")
print("tienes 10 intentos.")

continuar = "si"
while continuar.lower() == "si":
 # número secreto aleatorio entre 1 y 100
 numero_secreto = random.randint(1 , 100)


 Nintentos = 0
 adivina = False

 # Bucle de todo el proceso del juego 
 while not adivina and Nintentos < 10:
    num = input("Ingresa un número entre 1 y 100): ")
    
# numero fuera de 100 o menor de 1   
    if not num.isdigit():
        print("ingresa un número válido.")
        continue
    
    num = int(num)
    
    if num < 1 or num > 100:
        print("El número debe estar entre 1 y 100.")
        continue
    Nintentos += 1

    
    if num < numero_secreto:
        print("el numero es mayor.")
    elif num > numero_secreto:
        print("el numero es menor. ")
    else:
        print(f"¡WAO! ¡Adivinaste el número en {Nintentos} intentos!")
        adivina = True

    # Contador de intentos
    print(f"Intentos realizados: {Nintentos}")

 

 if adivina:
    print(f"¡Felicidades! ¡Adivinaste el número en {Numintentos} intentos!")
 else:
    print("No has adivinado el número en 10 intentos. El número secreto era: ", numero_secreto)

 continuar = input("¿Deseas continuar? (si/no): ")
 if continuar.lower() == "no":
    print("Hasta luego")

    #valerie lasso 