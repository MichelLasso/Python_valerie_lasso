#carrito

carrito = [] #Lista vacia

# Agregar un artículo al carrito

articulo = {"nombre": "Camiseta","precio": 20000,"cantidad": 5}
carrito.append(articulo)#guardar los articlos en la lista vacia carrito

# Imprimir el contenido del carrito
print("\nCARRITO\n")

for articulo in carrito:
  print(f"Nombre: {articulo['nombre']}, Precio: {articulo['precio']}, Cantidad: {articulo['cantidad']}\n")

#desarrollado por Valerie Lasso T.I 109326678