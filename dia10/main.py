import json

with open("info.json",encoding="utf-8") as openfile:
    miJson = json.load(openfile) 



def abrirArchivo():
        
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
        
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)

def mostrar_menu():#funcion para mostrar el menu de lo que se pede hacer con los estudiantes

    print("\nMenú de estudiantes:")
    print("1. Revisar el estudiante")
    print("2. Actualizar un dato del estudiante")
    print("3. Crear el estudiante ")
    print("4. Eliminar el estudiante")
    print("5. Salir del programa")
        
def dato():#funcion para mostrar los datos editables
    print("1. ID")
    print("2. nombre")
    print("3. apellido")
    print("4. edad")
    print("5. fecha de nacimiento")
    print("6. cedula")
    print("7. email")
    print("8. github")

print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")

bucle=True
while bucle==True:

    mostrar_menu()
    print("Hola! Por favor escoge alguna de las opciones: ")
    x=int(input("Cual opción escoges:"))
    miInfo=[]

    if x==1:

        miInfo=abrirArchivo()
        for i in miInfo[0]["estudiantes"]:
            print("################")
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("################")
            print("")

    elif x==2:

        print("\nACTUALIZAR UN DATO DEL ESTUDIANTE ")
        print("0. GRUPO T2\n1. GRUPO P1")

        num=int(input("ingresa el indice del estudiante"))


        if num==0: 
            estudiante = int(input("ingresa el número del estudiante que deseas a cambiar? (1/2)"))
            
            dato()

            dato_cambiar=int(input("\nQue dato deseas cambiar"))
                        
            if dato_cambiar==1:
                
                nuevo_id = input("Ingresa el nuevo id:")
                miJson[0]["estudiantes"][estudiante-1]["id"] = nuevo_id
                guardarArchivo(miJson)
                print("Cambio realizado!")
                            
            elif dato_cambiar==2: 

                nuevo_name = input("Ingresa el nuevo nombre:")
                miJson[0]["estudiantes"][estudiante-1]["nombre"] = nuevo_name
                guardarArchivo(miJson)
                print("Cambio realizado!")

            elif dato_cambiar==3:

                nuevo_apellido = input("Ingresa el nuevo apellido:")
                miJson[0]["estudiantes"][estudiante-1]["apellido"] = nuevo_apellido
                guardarArchivo(miJson)
                print("Cambio realizado!")

            elif dato_cambiar==4:

                nuevo_edad = input("Ingresa la nuevo edad:")
                miJson[0]["estudiantes"][estudiante-1]["edad"] = nuevo_edad
                guardarArchivo(miJson)
                print("Cambio realizado!")
            
            elif dato_cambiar==5:

                nuevo_fecha = input("Ingresa la nueva fecha de nacimiento :")
                miJson[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevo_fecha
                guardarArchivo(miJson)
                print("Cambio realizado!")

            elif dato_cambiar==6:

                nuevo_cedula = input("Ingresa la cedula nueva :")
                miJson[0]["estudiantes"][estudiante-1]["cedula"] = nuevo_cedula
                guardarArchivo(miJson)
                print("Cambio realizado!")
            
            elif dato_cambiar==7:
                
                nuevo_email = input("Ingresa la email nueva :")
                miJson[0]["estudiantes"][estudiante-1]["email"] = nuevo_email
                guardarArchivo(miJson)
                print("Cambio realizado!")
                
            elif dato_cambiar==8:

                nuevo_github = input("Ingresa la cedula nueva :")
                miJson[0]["estudiantes"][estudiante-1]["github"] = nuevo_github
                guardarArchivo(miJson)
                print("Cambio realizado!")
        
    elif x==3:
        nuevo_evento = {
        "id": input("Ingrese el ID del evento: "),
        "nombre": input("Ingrese el nombre: "),
        "apellido": input("ingrese el  apellido"),
        "edad": (input("Ingrese la edad: ")),
        "fecha de nacimiento": input("Ingrese la fecha de nacimiento: "),
        "cedula": input("Ingrese la cedula : "),
        "email": input("Ingrese el email: "),
        "github": input("Ingrese el githb: ")
        }
        with open("info.json","w") as outfile:
            json.dump(nuevo_evento,outfile)

    elif x==5:
        bucle==False

