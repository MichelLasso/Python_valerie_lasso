#programa fibonacci

print("BIENVENIDO AL PROGRAMA FIBONACCI")
print("")
print("En matemática, la sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa agregando números que son la suma de los dos anteriores : 0, 1, 1, 2, 3, 5, 8. , 13")
print("")

#iniciamos el bucle while para que se repita el proceso is el usuario lo desea
conti="s"
while conti.lower()=="s":
 
 numero=int(input(" ingresar un número entero, representando hasta qué término de la secuencia se generará: "))
 a=0
 b=1

 print("")
 for i in range (1,numero): #ciclo para los numeros
    while a<89: #para que sean 11 numeros
        print(a) #mostrar los numeros , en este caso se inicia desde 0
        break #terminar este bucle
    resu=a+b #formula finobacci, el numero que sigue es el resultado de los dos anteriores
    a=b
    b=resu

 conti=input("Desea continuar en el programa? (s/n)")#depende de la opcion del usuario se inicia nuevamente el programa o no
 if conti .lower()=="n":
    print("")
    print("Fin del programa :) ")

#desarrollado por Valerie Lasso C.I 1.093.296.678