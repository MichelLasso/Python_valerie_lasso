#-----------------------------------
#------Día 1 cheat sheet python-----
#-----------------------------------

#Imprimir Hola Mundo
print("Hola Mundo")


#Datos primitivos

#Número
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la información (input)

print("")

nombre = input("Por favor, ingrese su nombre: ")

print("")

#Conversión de tipos de variables

edad = "18"
print(edad)
print(type(edad))

print("")

int_edad = int(edad)
print(int_edad + 2) 
print(type(int_edad))

print("")

#int a bool 

numero=10
print(numero)
print(type(numero))

print("")

booleano= bool(numero)
print(booleano) 
print(type(booleano))#imprime el tipo
print("")
#Bucles For y While

#While
i = 0
while i < 10 :
  print(i**2)  
  i = i + 1
  print ("valerie")
print("")

#For

for i in range(10) :
  print(i**2)

print("")

#Funciones de cuatro tipos

# función sin parámetros o retorno de valores

def Saluda() :
    print("HOLAA") # llamada a la función y se muestra en la consola
Saluda()

# función con un parámetro

def saludos(name) :
    print("Hola " + name + ", que tengas un buen día")
    
saludos("valerie")

# función con múltiples parámetros con una sentencia de retorno

def suma(a , b) :
    suma= a + b
    return suma

rsuma = suma (2 , 3)

print("El resultado de la suma es: ", rsuma, )

#funcion sin parametros con retorno 

print("")
def suma(): 
   return "2"
print ("resultado es :",suma(),)


#Desarrollado por Valerie Lasso - C.I 1.093.296.678
