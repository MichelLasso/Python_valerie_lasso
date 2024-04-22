#funcion para calcular la posicion del número

def buscar_insertar(entrada, objetivo): #funcion de los numeros que hay y el n° que el usuario desea buscar

    izquierda, derecha = 0, len(entrada) #representa la posicion de los números en la fila <- medio -> / indica que la posicion empieza desde 0

    while izquierda < derecha: #si  izquierda sea menor que derecha, el algoritmo continúa buscando
        medio = (izquierda + derecha) // 2 #medio es el promedio de izquierda y derecha
        if entrada[medio] < objetivo: #comparar el valor que el usuario ingreso con el promedio de izquierda y derecha, si el n° que la persona ingreso es mayor se indica que es 
            izquierda = medio + 1 
        else:
            derecha = medio
    return izquierda

entrada=[1,3,5,7,9]

print("")
print(entrada)

objetivo = int(input("target: ")) 

print(buscar_insertar(entrada, objetivo))
print("")