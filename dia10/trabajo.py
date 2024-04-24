import json

with open("large-file.json",encoding="utf-8") as openfile:
    miJson = json.load(openfile)

CrearEvento=[]
WatchEvent=[]
PushEvent=[]
ForkEvent=[]
IssueCommentEvent=[]
PublicEvent=[]
ReleaseEvent=[]
IssuesEvent=[]
DeleteEvent=[]
PullRequestEvent=[]
MemberEvent=[]
GollumEvent=[]
PullRequestReviewCommentEvent=[]
CommitCommentEvent=[]

def mostrar_menu():

    print("Menú de Eventos:")
    print("1. Crear un dato del evento")
    print("2. Actualizar el dato del evento")
    print("3. Revisar el dato del Evento")
    print("4. Eliminar el dato del Evento")
    print("5. Salir del programa")

def eventos():
    print("1. WatchEvent")
    print("2. CreateEvent")
    print("3. PushEvent")
    print("4. ForkEvent")
    print("5. IssueCommentEvent")
    print("6. PublicEvent")
    print("7. ReleaseEvent")
    print("8. IssuesEvent")
    print("9. DeleteEvent")
    print("10. PullRequestEvent")
    print("11. MemberEvent")
    print("12. GollumEvent")
    print("13. PullRequestReviewCommentEvent")
    print("14. CommitCommentEvent")

def dato():
    print("\nACTOR")
    print("1. ID")
    print("2. login")
    print("3. avatar url")
    print("\nREPOSITORIO")
    print("4. ID")
    print("5. name")
    print("6. Public")

def id():
    print("CAMBIAR ID") 
    cambiar_id=int(input("ingrese el nuevo ID"))
    WatchEvent[num]["id"]=cambiar_id

    with open("eventos.json","w") as outfile:
        json.dump(WatchEvent,outfile)
    
           

#almacenar los datos json de cada evento en una nueva variable distinta para cada evento
for i in range (len(miJson)):
    if (miJson[i]["type"]=="WatchEvent"):
        WatchEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i] ["type"]=="CreateEvent"):
        CrearEvento.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="PushEvent"):
        PushEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="ForkEvent"):
        ForkEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="IssueCommentEvent"):
        IssueCommentEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="PublicEvent"):
        PublicEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="ReleaseEvent"):
        ReleaseEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="IssuesEvent"):
        IssuesEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="DeleteEvent"):
        DeleteEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="PullRequestEvent"):
        PullRequestEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="MemberEvent"):
        MemberEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="GollumEvent"):
        GollumEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="PullRequestReviewCommentEvent"):
        PullRequestReviewCommentEvent.append(miJson[i])

for i in range (len(miJson)):
    if (miJson[i]["type"]=="CommitCommentEvent"):
        CommitCommentEvent.append(miJson[i])

#mostrar menu de opciones / pedir la opcion al usuario

mostrar_menu()
opcion=int(input("ingresa la opcion que deseas realizar"))

if opcion==1:
    def crear_evento():
        nuevo_evento= {
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
        
    crear_evento()


elif opcion==2: 

    print("\nACTUALIZAR DATO DEL EVENTO")
    eventos()
    usuarioEvento=int(input("\nIngrese el número del evento que desea actualizar"))
        
    if usuarioEvento==1:

        print("\nDeseas modificar el evento WatchEvent")
            
        num=int(input("Ingrese un número para editar un dato de WatchEvent"))
        WatchEvent[num]
            
        dato()
        dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
        if dato_cambiar==1:
            id()
#valerie