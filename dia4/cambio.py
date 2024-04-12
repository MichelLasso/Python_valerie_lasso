#programa de cambio de dinero a monedas 1,5,10

def calcularCambio(cantidad):
    if cantidad<104:
        cambioUsuario = []
        
        # Calcular el número de monedas de 10 /operacion 1
        monedas10 = cantidad // 10 #dividir el n° que el usuario me dio en entero de 10
        cambioUsuario.append(monedas10) #almacenar el n° que me dio en la formula anterior en la variable cambioUsuario con el .append
        cantidad -= monedas10 * 10 #El resultado de la primera formula se multiplica por el 10 y el resultado se le resta al dato que el usuario ingreso
            
        # Calcular el número de monedas de 5  /operacion 2
        #aqui en cantidad ya no es el n° que el usuario ingreso, sino qu es el n° que quedo en la ultima operacion de arriba
        monedas5 = cantidad // 5
        cambioUsuario.append(monedas5)
        cantidad -= monedas5 * 5
            
        # Calcular el número de monedas de 1 / /operacion 3
        monedasde1 = cantidad #el n° de monedas restantes se define en monedas 1 y muestra la cantidad del número que queda, si queda 5 muestra 5 monedas de 1
        cambioUsuario.append(monedasde1)
            
        return cambioUsuario 

print("")
print("CAMBIO DE MONEDA---1, 5, 10")
print("")
print("el número que ingrese debe ser menor a 104 o el programa no ejecutara")
print("")
cantidad=int(input("Ingrese el numero que desea cambiar a la moneda (1,5,10): ")) # Cambio a calcular
cambioUsuario = calcularCambio(cantidad) #llamar la funcion calcularCambio
print("")
print(f"Para {cantidad}, el cambio es: ") #mostrar al usuario el n° que ingreso
print(f"{cambioUsuario[0]} monedas de 10") #mostrar el cambio en monedas de 10
print(f"{cambioUsuario[1]} monedas de 5") #mostrar el cambio en monedas de 5
print(f"{cambioUsuario[2]} monedas de 1") #mostrar el cambio en monedas de 1
print("")
print("GRACIAS POR USAR EL CAMBIO DE MONEDA---1, 5, 10")#despedida
print("")

print("BayBay :)")
