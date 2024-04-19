carrito=[]
articulos=[]

print("TIENDA")
#menú
print("1. Café----1000")
print("2. frapuchino----7000")
print("3. Agua----500")

#el usuario debe ingresar el numero del articulo que desea
nameP=int(input("Ingrese el numero del articulo  que deseas agregar"))
if nameP==1:
    
    cantidad=int(input("cuántos deseas comprar?"))
    
    precioUsuario=cantidad*1000 #dependiendo de la cantidad que el usuario compre se multiplica por el precio
   
    print("Tu producto tiene un precio de: ",precioUsuario)#mostrar al usuario el total de su compra
    
    articulos=[nameP,precioUsuario,cantidad]#guardar en la lista articulos los datos del usuario
    carrito.append(articulos)#los datos del usuario almacenados anteriormente se guarda en la lista carrito

    for articulos in carrito: 

        print("\nNombre--N° en menú--Precio--Cantidad")
        print("Café ",carrito)#mostrar al usuario su compra
        
    print("\nGRACIAS POR SU COMPRA")
    

if nameP==2:

    cantidad=int(input("cuántos deseas comprar?"))
    
    precioUsuario=cantidad*7000
   
    print("Tu producto tiene un precio de: ",precioUsuario)
   
    articulos=[nameP,precioUsuario,cantidad]
    carrito.append(articulos)

    for articulos in carrito:

        print("\nNombre--N° en menú--Precio--Cantidad")
        print("frapuchino ",carrito)
        
    print("\nGRACIAS POR SU COMPRA")

if nameP==3:

    cantidad=int(input("cuántos deseas comprar?"))
    
    precioUsuario=cantidad*500
   
    print("Tu producto tiene un precio de: ",precioUsuario)
    
    articulos=[nameP,precioUsuario,cantidad]
    carrito.append(articulos)

    for articulos in carrito:

        print("\nNombre--N° en menú--Precio--Cantidad")
        print("Agua ",carrito)
        
    print("\nGRACIAS POR SU COMPRA")

#desarrollado por Valerie Lasso T.I 1093296678
