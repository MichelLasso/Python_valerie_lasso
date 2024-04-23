import json 
archivo_json="large-file.json"
with open(archivo_json,encoding="utf-8")as archivo:
    datos_json=json.load(archivo)

def mostrar_menu():

    print("Menú de Eventos:")
    print("1. Crear Evento")
    print("2. Actualizar Evento")
    print("3. Revisar Evento")
    print("4. Eliminar Evento")
    print("5. Salir")

def crear_evento(eventos):
    nuevo_evento = {
        "id": int(input("Ingrese el ID del evento: ")),
        "type": input("Ingrese el tipo de evento: "),
        "actor": {
            "id": int(input("Ingrese el ID del actor: ")),
            "login": input("Ingrese el login del actor: "),
            "gravatar_id": input("Ingrese el gravatar_id del actor (opcional): "),
            "url": input("Ingrese la URL del actor: "),
            "avatar_url": input("Ingrese la avatar_url del actor: ")
        }
    }
    eventos.append(nuevo_evento)
    guardar_eventos=(eventos)
    print("Evento creado exitosamente.")


mostrar_menu()
a=int(input("ingresa la opcion que deseas ralizar"))

if a==1:

    print("\nCREAR EVENTO\n")
    crear_evento("eventos")

elif a==2:
    print("ACTUALIZAR EVENTO\n")


