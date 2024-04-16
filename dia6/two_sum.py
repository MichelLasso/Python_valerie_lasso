def dossumas(nums, target): #funcion
    almacenar = {}

    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in almacenar:
            return [almacenar[complemento], i]
        almacenar[num] = i
    return print("No hay números en la lista que sumados den el número que ingresaste")

print("TOWN SUM")
print("")

nums = [2,7,11,15,3,4]#numeros almacenados en una lista

target=int(input("Ingrese un número: "))#el usuario ingresa un numero

print("")
print(nums)
print("")
print(dossumas(nums, target)) #muestra la posicion del número qe se sumo y dió como resultado el numero que el usuario ingreso

#desarrollado por Valerie Lasso C.I 1093296678