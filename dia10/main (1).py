import json #llamar el json

#guadar el  archivo json en una variable llamada miJson
with open("large-file.json",encoding="utf-8") as openfile:
    miJson = json.load(openfile) 

#guardar los eventos en una variable / para cada evento una variable distinta
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

new=[]
nuevo_evento=[]

def mostrar_menu():#funcion para mostrar el menu de lo que se pede hacer co los eventos

    print("\nMenú de Eventos:")
    print("1. Crear un dato del evento")
    print("2. Actualizar el dato del evento")
    print("3. Revisar el dato del Evento")
    print("4. Eliminar el dato del Evento")#falta
    print("5. Salir del programa")

def eventos():#funcion para mostrar los eventos
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

def dato():#funcion para mostrar los datos editables
    print("\nACTOR")
    print("1. ID")
    print("2. login")
    print("3. avatar url")
    print("\nREPOSITORIO")
    print("4. ID")
    print("5. name")
    print("6. Public")

def crear_evento():

    nuevo_evento = {
        "id": input("Ingrese el ID del evento: "),
        "type": input("Ingrese el tipo de evento: "),
        "actor": {
            "id": (input("Ingrese el ID del actor: ")),
            "login": input("Ingrese el login del actor: "),
            "gravatar_id": input("Ingrese el gravatar_id del actor : "),
            "url": input("Ingrese la URL del actor: "),
            "avatar_url": input("Ingrese la avatar_url del actor: ")
        }
    }
    with open("eventos.json","w") as outfile:
        json.dump(nuevo_evento,outfile)
    

#almacenar los datos json de cada evento en una nueva variable distinta para cada evento

bucle=True
while bucle==True:

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


    mostrar_menu()#mostrar menu de opciones / pedir la opcion al usuario
    opcion=int(input("ingresa la opcion que deseas realizar "))

    if opcion==1:

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

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                WatchEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(WatchEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                WatchEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                WatchEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(WatchEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                WatchEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(WatchEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                WatchEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(WatchEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                WatchEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(WatchEvent,outfile)

                if public_cambiar=="true":

                    WatchEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    WatchEvent[num]["public"]=public_cambiar

        elif usuarioEvento==2:

            print("\nDeseas modificar el evento CreatEvent")
                
            num=int(input("Ingrese un número para editar un dato de CreatEvent"))
            CrearEvento[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                CrearEvento[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(CrearEvento,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                CrearEvento[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                CrearEvento[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(CrearEvento,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                CrearEvento[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(CrearEvento,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                CrearEvento[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(CrearEvento,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                CrearEvento[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(CrearEvento,outfile)

                if public_cambiar=="true":

                    CrearEvento[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    CrearEvento[num]["public"]=public_cambiar

        elif usuarioEvento==3:

            print("\nDeseas modificar el evento PushEvent")
                
            num=int(input("Ingrese un número para editar un dato de PushEvent"))
            PushEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                PushEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PushEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                PushEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                PushEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(PushEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                PushEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PushEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                PushEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(PushEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                PushEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(PushEvent,outfile)

                if public_cambiar=="true":

                    PushEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    PushEvent[num]["public"]=public_cambiar

        elif usuarioEvento==4:

            print("\nDeseas modificar el evento ForkEvent")
                
            num=int(input("Ingrese un número para editar un dato de ForkEvent"))
            ForkEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                ForkEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(ForkEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                ForkEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                ForkEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(ForkEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                ForkEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(ForkEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                ForkEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(ForkEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                ForkEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(ForkEvent,outfile)

                if public_cambiar=="true":

                    ForkEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    ForkEvent[num]["public"]=public_cambiar

        elif usuarioEvento==5:

            print("\nDeseas modificar el evento IssueCommentEvent")
                
            num=int(input("Ingrese un número para editar un dato de IssueCommentEvent"))
            IssueCommentEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                IssueCommentEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(IssueCommentEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                IssueCommentEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                IssueCommentEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(IssueCommentEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                IssueCommentEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(IssueCommentEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                IssueCommentEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(IssueCommentEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                IssueCommentEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(IssueCommentEvent,outfile)

                if public_cambiar=="true":

                    IssueCommentEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    IssueCommentEvent[num]["public"]=public_cambiar

        elif usuarioEvento==6:

            print("\nDeseas modificar el evento PublicEvent")
                
            num=int(input("Ingrese un número para editar un dato de PublicEvent"))
            PublicEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                PublicEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PublicEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                PublicEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                PublicEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(PublicEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                PublicEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PublicEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                PublicEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(PublicEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                PublicEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(PublicEvent,outfile)

                if public_cambiar=="true":

                    PublicEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    PublicEvent[num]["public"]=public_cambiar         
        
        elif usuarioEvento==7:

            print("\nDeseas modificar el evento ReleaseEvent")
                
            num=int(input("Ingrese un número para editar un dato de ReleaseEvent"))
            ReleaseEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                ReleaseEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(ReleaseEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                ReleaseEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                ReleaseEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(ReleaseEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                ReleaseEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(ReleaseEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                ReleaseEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(ReleaseEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                ReleaseEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(ReleaseEvent,outfile)

                if public_cambiar=="true":

                    ReleaseEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    ReleaseEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==8:

            print("\nDeseas modificar el evento IssuesEvent")
                
            num=int(input("Ingrese un número para editar un dato de IssuesEvent"))
            IssuesEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                IssuesEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(IssuesEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                IssuesEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                IssuesEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(IssuesEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                IssuesEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(IssuesEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                IssuesEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(IssuesEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                IssuesEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(IssuesEvent,outfile)

                if public_cambiar=="true":

                    IssuesEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    IssuesEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==9:

            print("\nDeseas modificar el evento DeleteEvent")
                
            num=int(input("Ingrese un número para editar un dato de DeleteEvent"))
            DeleteEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                DeleteEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(DeleteEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                DeleteEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                DeleteEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(DeleteEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                DeleteEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(DeleteEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                DeleteEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(DeleteEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                DeleteEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(DeleteEvent,outfile)

                if public_cambiar=="true":

                    DeleteEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    DeleteEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==10:

            print("\nDeseas modificar el evento PullRequestEvent")
                
            num=int(input("Ingrese un número para editar un dato de PullRequestEvent"))
            PullRequestEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                PullRequestEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PullRequestEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                PullRequestEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(PullRequestEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                PullRequestEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(PullRequestEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                PullRequestEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PullRequestEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                PullRequestEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(PullRequestEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                PullRequestEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(PullRequestEvent,outfile)

                if public_cambiar=="true":

                    PullRequestEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    PullRequestEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==11:

            print("\nDeseas modificar el evento MemberEvent")
                
            num=int(input("Ingrese un número para editar un dato de MemberEvent"))
            MemberEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                MemberEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(MemberEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                MemberEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                MemberEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(MemberEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                MemberEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(MemberEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                MemberEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(MemberEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                MemberEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(MemberEvent,outfile)

                if public_cambiar=="true":

                    MemberEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    MemberEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==12:

            print("\nDeseas modificar el evento GollumEvent")
                
            num=int(input("Ingrese un número para editar un dato de GollumEvent"))
            GollumEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                GollumEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(GollumEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                GollumEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(GollumEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                GollumEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(GollumEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                GollumEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(GollumEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                GollumEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(GollumEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                GollumEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(GollumEvent,outfile)

                if public_cambiar=="true":

                    GollumEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    GollumEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==13:

            print("\nDeseas modificar el evento PullRequestReviewCommentEvent")
                
            num=int(input("Ingrese un número para editar un dato de PullRequestReviewCommentEvent"))
            PullRequestReviewCommentEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                PullRequestReviewCommentEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PullRequestReviewCommentEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                PullRequestReviewCommentEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                PullRequestReviewCommentEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(PullRequestReviewCommentEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                PullRequestReviewCommentEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(PullRequestReviewCommentEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                PullRequestReviewCommentEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(PullRequestReviewCommentEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                PullRequestReviewCommentEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(PullRequestReviewCommentEvent,outfile)

                if public_cambiar=="true":

                    PullRequestReviewCommentEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    PullRequestReviewCommentEvent[num]["public"]=public_cambiar    

        elif usuarioEvento==14:

            print("\nDeseas modificar el evento CommitCommentEvent")
                
            num=int(input("Ingrese un número para editar un dato de CommitCommentEvent"))
            CommitCommentEvent[num]
                
            dato()
            dato_cambiar=int(input("\nQue dato deseas cambiar"))
            
            if dato_cambiar==1:

                print("CAMBIAR ID DEL ACTOR") 
                cambiar_id=input("ingrese el nuevo ID")
                CommitCommentEvent[num]["actor"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(CommitCommentEvent,outfile)


            elif dato_cambiar==2:

                print("\nCAMBIAR LOGIN  DEL ACTOR")
                login_cambiar=input("ingrese el nuevo login ")
                CommitCommentEvent[num]["actor"]["login"]=login_cambiar

                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)


            elif dato_cambiar==3:

                print("\n CAMBIAR AVATAR URL  DEL ACTOR")    
                cambiar_avatar_url=(input("ingrese el nuevo url del avatar "))
                CommitCommentEvent[num]["actor"]["avatar_url"]=cambiar_avatar_url

                with open ("eventos.json","w") as outfile:
                    json.dump(CommitCommentEvent,outfile)
            
            elif dato_cambiar==4:

                print("CAMBIAR ID DEL REPOSITORIO ") 
                cambiar_id=(input("ingrese el nuevo ID"))
                CommitCommentEvent[num]["repo"]["id"]=cambiar_id

                with open("eventos.json","w") as outfile:
                    json.dump(CommitCommentEvent,outfile)

            elif dato_cambiar==5:

                print("\nCAMBIAR NAME  DEL ACTOR")
                name_cambiar=input("ingrese el nuevo name ")
                CommitCommentEvent[num]["repo"]["name"]=name_cambiar

                with open ("eventos.json","w") as outfile:
                    json.dump(CommitCommentEvent,outfile)
            
            elif dato_cambiar==6:
                 
                print("\nCAMBIAR PUBLIC  DEL ACTOR")
                public_cambiar=input("ingrese si quiere que sea publico o no\ntrue\nfalse ")
                CommitCommentEvent[num]["public"]=public_cambiar

                with open ("eventos.json","w") as outfile:
                        json.dump(CommitCommentEvent,outfile)

                if public_cambiar=="true":

                    CommitCommentEvent[num]["public"]=public_cambiar

                elif public_cambiar=="false":

                    CommitCommentEvent[num]["public"]=public_cambiar 

    elif opcion==3:

        print("\nREVISAR EL DATO DEL EVENTO")
        eventos()
        revisar=int(input("\nIngrese el número del evento que desea revisar"))

        if revisar==1:
            print("\nDeseas revisa el evento WatchEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento WatchEvent"))
            WatchEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",WatchEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",WatchEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",WatchEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",WatchEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",WatchEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", WatchEvent[revisar]["public"])
        
        if revisar==2:
            
            print("\nDeseas revisa el evento CreateEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento CreateEvent"))
            CrearEvento[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",CrearEvento[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",CrearEvento[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",CrearEvento[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",CrearEvento[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",CrearEvento[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", CrearEvento[revisar]["public"])
        
        if revisar==3:

            print("\nDeseas revisa el evento PushEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento PushEvent"))
            PushEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",PushEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",PushEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",PushEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",PushEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",PushEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", PushEvent[revisar]["public"])
        
        if revisar==4:

            print("\nDeseas revisa el evento ForkEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento ForkEvent"))
            ForkEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",ForkEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",ForkEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",ForkEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",ForkEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",ForkEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", ForkEvent[revisar]["public"])
        
        if revisar==5:

            print("\nDeseas revisa el evento IssueCommentEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento IssueCommentEvent"))
            IssueCommentEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",IssueCommentEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",IssueCommentEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",IssueCommentEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",IssueCommentEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",IssueCommentEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", IssueCommentEvent[revisar]["public"])
        
        if revisar==6:

            print("\nDeseas revisa el evento PublicEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento PublicEvent"))
            PublicEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",PublicEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",PublicEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",PublicEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",PublicEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",PublicEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", PublicEvent[revisar]["public"])
        
        if revisar==7:

            print("\nDeseas revisa el evento ReleaseEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento ReleaseEvent"))
            ReleaseEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",ReleaseEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",ReleaseEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",ReleaseEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",ReleaseEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",ReleaseEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", ReleaseEvent[revisar]["public"])
        
        if revisar==8:

            print("\nDeseas revisa el evento IssuesEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento IssuesEvent"))
            IssuesEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",IssuesEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",IssuesEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",IssuesEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",IssuesEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",IssuesEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", IssuesEvent[revisar]["public"])

        if revisar==9:

            print("\nDeseas revisa el evento DeleteEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento DeleteEvent"))
            DeleteEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",DeleteEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",DeleteEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",DeleteEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",DeleteEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",DeleteEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", DeleteEvent[revisar]["public"])

        if revisar==10:

            print("\nDeseas revisa el evento PullRequestEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento PullRequestEvent"))
            PullRequestEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",PullRequestEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",PullRequestEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",PullRequestEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",PullRequestEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",PullRequestEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", PullRequestEvent[revisar]["public"])

        if revisar==11:

            print("\nDeseas revisa el evento MemberEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento MemberEvent"))
            MemberEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",MemberEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",MemberEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",MemberEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",MemberEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",MemberEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", MemberEvent[revisar]["public"])

        if revisar==12:

            print("\nDeseas revisa el evento GollumEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento GollumEvent"))
            GollumEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",GollumEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",GollumEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",GollumEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",GollumEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",GollumEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", GollumEvent[revisar]["public"])


        if revisar==13:

            print("\nDeseas revisa el evento PullRequestReviewCommentEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento PullRequestReviewCommentEvent"))
            PullRequestReviewCommentEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",PullRequestReviewCommentEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",PullRequestReviewCommentEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",PullRequestReviewCommentEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",PullRequestReviewCommentEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",PullRequestReviewCommentEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", PullRequestReviewCommentEvent[revisar]["public"])

        if revisar==14:

            print("\nDeseas revisa el evento CommitCommentEvent")
                
            num_revisar=int(input("Ingrese un número para revisar el dato del evento CommitCommentEvent"))
            CommitCommentEvent[num_revisar]

            dato()
            dato_revisar=int(input("\nQue dato deseas revisar?"))

            if dato_revisar==1: 

                print("El ID del actor es :",CommitCommentEvent[revisar]["actor"]["id"])

            elif dato_revisar==2:

                print("El login del actor es :",CommitCommentEvent[revisar]["actor"]["login"])
            
            elif dato_revisar==3:

                print("El avatar url del actor es: ",CommitCommentEvent[revisar]["actor"]["avatar_url"])

            elif dato_revisar==4:

                print("El id del repositori es : ",CommitCommentEvent[revisar]["repo"]["id"])
            
            elif dato_revisar==5:

                print("El nombre del repositorio es :",CommitCommentEvent[revisar]["repo"]["name"])

            elif dato_revisar==6:

                print("E repositorio es : ", CommitCommentEvent[revisar]["public"])

    elif opcion==4:

        print("\n ELIMINAR EL DATO DEL EVENTO")
        eventos()
        
        eliminar=int(input("\nIngrese el número del evento que desea eliminar"))

        
        if eliminar==1:
            print("\nDeseas eliminar el evento WatchEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento WatchEvent"))
            WatchEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del WatchEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del WatchEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del WatchEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del WatchEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del WatchEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del WatchEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(WatchEvent,a)

                print("\nEliminado con éxito")

        if eliminar==2:

            print("\nDeseas eliminar el evento CreateEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento CreateEvent"))
            CrearEvento[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del CrearEvento[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del CrearEvento[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del CrearEvento[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del CrearEvento[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del CrearEvento[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del CrearEvento[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CrearEvento,a)

                print("\nEliminado con éxito")

        if eliminar==3:

            print("\nDeseas eliminar el evento PushEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento PushEvent"))
            PushEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del PushEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PushEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PushEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PushEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del PushEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PushEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PushEvent,a)

                print("\nEliminado con éxito")

        if eliminar==4:

            print("\nDeseas eliminar el evento ForkEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento ForkEvent"))
            ForkEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del ForkEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del ForkEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del ForkEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del ForkEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del ForkEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del ForkEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ForkEvent,a)

                print("\nEliminado con éxito")

        if eliminar==5:

            print("\nDeseas eliminar el evento IssueCommentEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento IssueCommentEvent"))
            IssueCommentEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del IssueCommentEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del IssueCommentEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del IssueCommentEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del IssueCommentEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del IssueCommentEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del IssueCommentEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssueCommentEvent,a)

                print("\nEliminado con éxito")

        if eliminar==6:

            print("\nDeseas eliminar el evento PublicEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento PublicEvent"))
            PublicEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del PublicEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PublicEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PublicEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PublicEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del PublicEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PublicEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PublicEvent,a)

                print("\nEliminado con éxito")

        if eliminar==7:

            print("\nDeseas eliminar el evento ReleaseEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento ReleaseEvent"))
            ReleaseEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del ReleaseEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del ReleaseEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del ReleaseEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del ReleaseEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del ReleaseEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del ReleaseEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(ReleaseEvent,a)

                print("\nEliminado con éxito")

        
        if eliminar==8:

            print("\nDeseas eliminar el evento IssuesEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento IssuesEvent"))
            IssuesEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del IssuesEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del IssuesEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del IssuesEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del IssuesEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del IssuesEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del IssuesEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(IssuesEvent,a)

                print("\nEliminado con éxito")

        if eliminar==9:

            print("\nDeseas eliminar el evento DeleteEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento DeleteEvent"))
            DeleteEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del DeleteEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del DeleteEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del DeleteEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del DeleteEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del DeleteEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del DeleteEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")

        if eliminar==10:

            print("\nDeseas eliminar el evento PullRequestEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento PullRequestEvent"))
            PullRequestEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del PullRequestEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(PullRequestEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PullRequestEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(PullRequestEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PullRequestEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PullRequestEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del PullRequestEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del DeleteEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(DeleteEvent,a)

                print("\nEliminado con éxito")

        if eliminar==11:

            print("\nDeseas eliminar el evento MemberEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento MemberEvent"))
            MemberEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del MemberEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del MemberEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del MemberEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del MemberEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del MemberEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del MemberEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

        if eliminar==12:

            print("\nDeseas eliminar el evento GollumEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento GollumEvent"))
            GollumEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del GollumEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(GollumEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del GollumEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(GollumEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del GollumEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(GollumEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del MemberEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del MemberEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del MemberEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(MemberEvent,a)

                print("\nEliminado con éxito")

        if eliminar==13:

            print("\nDeseas eliminar el evento PullRequestReviewCommentEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento PullRequestReviewCommentEvent"))
            PullRequestReviewCommentEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del PullRequestReviewCommentEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PullRequestReviewCommentEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del PullRequestReviewCommentEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PullRequestReviewCommentEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del PullRequestReviewCommentEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del PullRequestReviewCommentEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(PullRequestReviewCommentEvent,a)

                print("\nEliminado con éxito")

        if eliminar==14:

            print("\nDeseas eliminar el evento CommitCommentEvent")
                
            num_eliminar=int(input("Ingrese un número para eliminar el dato del evento CommitCommentEvent"))
            CommitCommentEvent[num_eliminar]

            dato()
            dato_eliminar=int(input("\nQue dato deseas eliminar?"))

            if dato_eliminar==1: 
                
                print("\nDESEAS ELIMINAR EL ID DEL ACTOR")
                del CommitCommentEvent[num_eliminar]["actor"]["id"]

                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==2:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del CommitCommentEvent[num_eliminar]["actor"]["login"]

                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==3:
                
                print("\nDESEAS ELIMINAR EL LOGIN DEL ACTOR")
                del CommitCommentEvent[num_eliminar]["actor"]["avatar_url"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==4:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del CommitCommentEvent[num_eliminar]["repo"]["id"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)

                print("\nEliminado con éxito")

            if dato_eliminar==5:

                print("\nDESEAS ELIMINAR EL NOMBRE DEL REPOSITORIO")
                del CommitCommentEvent[num_eliminar]["repo"]["name"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)

                print("\nEliminado con éxito")
            
            if dato_eliminar==6:

                print("\nDESEAS ELIMINAR EL ID DEL REPOSITORIO")
                del CommitCommentEvent[num_eliminar]["public"]
                
                with open ("eventos.json","w") as a:
                    json.dump(CommitCommentEvent,a)

                print("\nEliminado con éxito")
                
    elif opcion==5:
        bucle=False

        print("\nGracias por usar este programa :)")
    #valerie

    