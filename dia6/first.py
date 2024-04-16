entrada=[]#lista para almacenar los datos que ingrese el usuario

print("")
print("REMOVE DUPLICATES FROM SORTED LIST")
print("")

dato=int(input("ingrese la cantidad de datos: "))#se muestra el texto al usuario y se le pide la cantidad de números que desea ingresar

assert 0< dato <300,"ERROR,ingresaste un número fuera del límite (max 300)"#el dato del usuario debe tener un límite, y con el assert podemos definir el límite

for i in range (0,dato): #ciclo for para que el usuario ingrese los datos segun la cantidad que eligio anteriormente
    entrada.append(input("ingresa los datos"))#con el .append almacenamos los datos que el usuario ingresó  en la variable entrada

eliminar= list (set(entrada)) #en esta línea usamos el  set para eliminar los datos repetidos del usuario en la variable entrada
eliminar.sort()# en esta línea usamos el sort para organizar los datos de menor a mayor
print(eliminar) #mostrar al usuario los datos que ingresó de manera ordenada 

#desarrollado por Valerie Lasso C.I 1093296678