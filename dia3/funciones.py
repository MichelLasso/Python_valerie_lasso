#programa donde realizaremos varias funciones
def primo(nUsuario):
    if nUsuario <= 1:
        return "no es primo"
    elif nUsuario == 2:
        return "es primo"
    else:
        for i in range( 2, nUsuario):
            if nUsuario % i == 0:
                return "no es primo"
        return "es primo"

print("")
print("BIENVENIDO AL PROGRAMA DE 2 FUNCIONES")
print("")
print("MENÚ FUNCIONES : ")
print("1. Es un número primo?")
print("2. Generador de contraseñas")
menu_inicial=input("Ingrese un número para realizar una opcion del MENÚ FUNCIONES ")
if menu_inicial=="1":
    print("")
    print("ES UN NÚMERO PRIMO?")
    print("")
    print("Bienvenido, en este programa vamos a verificar si el número que ingresaste es primo o no.")
    print("")
    para=True
    while para==True:
        print("")
        print("1. Verificar un número")
        print("2. informacion adicional")
        print("3. Detener el programa  ")
        print("")

        menuUsuario=input("Elije un número, para realizar una opción del menú\n")
        
        if menuUsuario=="1":
            print("")
            nUsuario=int(input("Ingrese un número para saber si es primo o no\n "))
            print("el número",nUsuario,primo(nUsuario))
        
        if menuUsuario=="2":
            print("")
            print("¿QUE ES UN NÚMERO PRIMO?")
            print("")
            print("Un número primo es aquel que solo tiene dos divisores positivos distintos: él mismo y el número 1. Esto significa que si intentas dividirlo por cualquier otro número, el resultado no es un número entero, sino que se obtiene un resto distinto de cero. Por ejemplo, el número 7 es primo porque solo puede ser dividido por 1 y por sí mismo (7), sin dejar residuo. El número 1, por otro lado, no se considera primo porque tiene un solo divisor, que es él mismo. La existencia de números primos es infinita, lo cual fue demostrada por el matemático griego Eratóstenes mediante la Criba de Eratóstenes, un procedimiento que permite obtener todos los números primos hasta un número dado")
            print("Creador del programa: Valerie Lasso")
        
        if menuUsuario=="3":
            break
    para=False
if menu_inicial=="2":
 print("hola")