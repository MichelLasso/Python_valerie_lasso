carrito=[]
articulos=[]
print("TIENDA")

print("1. Café----1000")
print("2. frapuchino----7000")
print("3. Agua----500")

nameP=int(input("Ingrese el numero del articulo  que deseas agregar"))
if nameP==1:
    
    cantidad=int(input("cuántos deseas comprar?"))
    
    precioUsuario=cantidad*1000
   
    print("Tu producto tiene un precio de: ",precioUsuario)
    
    articulos=[nameP,precioUsuario,cantidad]
    carrito.append(articulos)

    for articulos in carrito: 

        print("\nNombre--N° en menú--Precio--Cantidad")
        print("Café ",carrito)
        
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

#desarrollado por Valerie Lasso
