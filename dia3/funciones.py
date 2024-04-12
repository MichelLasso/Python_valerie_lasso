#programa donde realizaremos varias funciones
def primo(nUsuario):#funcion para el numero primo
    if nUsuario <= 1: #si es uno, pues no es primo
        return "no es primo"
    elif nUsuario == 2: #si es 2 es primo
        return "es primo"
    else:
        for i in range( 2, nUsuario):#ciclo for q usamos para que nos lea el numero que el usuario ingreso y nos diga si es primo o no
            if nUsuario % i == 0: #formula para sacar el numero no primo
                return "no es primo" #resultado de la formula anterior
        return "es primo" #resultado de si es lo contrario a la formula anterior

print("")#espacio entre textos
print("BIENVENIDO AL PROGRAMA DE 2 FUNCIONES")#titulo
print("")
print("MENÚ FUNCIONES : ")
print("1. Es un número primo?")
print("2. Generador de contraseñas")

menu_inicial=input("Ingrese un número para realizar una opcion del MENÚ FUNCIONES ")#mostrar texto al usuario y pedirle el dato

if menu_inicial=="1":#segun el dato elegido por el usuario hacer
    print("")
    print("ES UN NÚMERO PRIMO?")
    print("")
    print("Bienvenido, en este programa vamos a verificar si el número que ingresaste es primo o no.")
    print("")
    
    para=True#el nombre de la variable que me inicial y finaliza el bucle while
    
    while para==True:
        print("")
        print("1. Verificar un número")
        print("2. informacion adicional")
        print("3. Detener el programa  ")
        print("")

        menuUsuario=input("Elije un número, para realizar una opción del menú\n")#mostrar texto y pedir el dato al usuario
        
        if menuUsuario=="1":#dato del usuario/hacer,en este caso 1
            print("")
            nUsuario=int(input("Ingrese un número para saber si es primo o no\n "))#mostrar texto y pedir dato al usuario
            print("el número",nUsuario,primo(nUsuario))#mostrar texto al usuario/llamamos la funcion del numero primo
        
        if menuUsuario=="2":#dato del usuario/hacer,en este caso 2
            print("")
            print("¿QUE ES UN NÚMERO PRIMO?")
            print("")
            print("Un número primo es aquel que solo tiene dos divisores positivos distintos: él mismo y el número 1. Esto significa que si intentas dividirlo por cualquier otro número, el resultado no es un número entero, sino que se obtiene un resto distinto de cero. Por ejemplo, el número 7 es primo porque solo puede ser dividido por 1 y por sí mismo (7), sin dejar residuo. El número 1, por otro lado, no se considera primo porque tiene un solo divisor, que es él mismo. La existencia de números primos es infinita, lo cual fue demostrada por el matemático griego Eratóstenes mediante la Criba de Eratóstenes, un procedimiento que permite obtener todos los números primos hasta un número dado")
            print("Creador del programa: Valerie Lasso")
        
        if menuUsuario=="3":#dato del usuario/hacer,en este caso 3
           
            break
   
    para=False#fin del ciclo

if menu_inicial=="2":
  
  import string  # Imprimir constantes del módulo string Mayúscula, minusculas, numeros
  
  import random 

def contraseñaTiene(longitud, minusculas, mayusculas, numeros, especiales):
        
        caracteres = "" #variable lista para almacenar los datos/esta vacia 
       
        if minusculas:
            caracteres += string.ascii_lowercase #unir los datos en minúscula a caracteres 
        
        if mayusculas:
            caracteres += string.ascii_uppercase  #unir los datos en mayuscula a caracteres 
        
        if numeros:
            caracteres += string.digits #unir digitos a caracteres 
       
        if especiales:
            caracteres += string.punctuation #Unir datos especiales a caracteres 

        
        
        contraseñas = ""#variable lista para almacenar datos
        
        for i in range(longitud):
            
            contraseñas += random.choice(caracteres)#crear una contraseña con datos al azar almacenados en caracteres 
        return contraseñas
    


continuar = "si"

while continuar.lower() == "si": #ciclo de contraseña/el usuario decide si desea continuar 
        
        print("CREA TU CONTRASEÑA CON NOSOTROS")#titulo
        print("")
        print("¿Qué es un generador de contraseñas")
        print("")
        print("Un generador de contraseñas es una herramienta que crea combinaciones aleatorias de letras, números y símbolos para formar contraseñas seguras y difíciles de adivinar. Estas contraseñas son útiles para proteger cuentas en línea, ya que son más difíciles de hackear que contraseñas simples o predecibles. Al usar un generador de contraseñas, puedes asegurarte de que tus cuentas estén mejor protegidas contra posibles ataques cibernéticos.")#mostrar texto al usuario acera de el generador de contraseñas
        print("")
            
        longitud = int(input("¿Cúal es la longitud que deseas para tu contraseña segura:"))#mostrar texto y pedir dato al usuario
        print("")
        
        minusculas = input("¿Quieres que tu contraseña contenga minúsculas?(si/no)").lower() == "si" #mostrar texto y pedir dato al usuario
        print("")
        
        mayusculas = input("¿Quieres que tu contraseña contenga mayúsculas?(si/no)").lower() == "si" #mostrar texto y pedir dato al usuario
        print("")
        
        numeros = input("¿Quieres que tu contraseña contenga números?(si/no)").lower() == "si"#mostrar texto y pedir dato al usuario
        print("")
        
        especiales = input("¿Quieres que tu contraseña contenga caracteres especiales?(si/no)\n").lower() == "si" #mostrar texto y pedir dato al usuario
        print("")
        
        contraseñaUsuario= contraseñaTiene(longitud, minusculas, mayusculas, numeros, especiales)#lo que debe tener la contraseña , segun lo que pidio el usuario
        
        print("")
        print("Su contraseña segura es :", contraseñaUsuario)#mostrar la contraseña
        print("")
        
        continuarUsuario = input("Desea crear otra contraseña(si/no)")

        if  continuarUsuario == "no":#si el usuario no quiere seguir con el programa se cierra el ciclo 
            
            print("")
            print("Gracias por usar el generador de contraseñas :) ")
            print("Bay Bay")
            
            break #parar el bucle
        
#Desarrollado por Valerie Lasso C.I 1093296678