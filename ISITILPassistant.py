
def extra_space_remover(stringa):
    temp = ""
    space = False
    for x in stringa:
        if x == " " and space == True:
            continue
        elif x == " " and space == False:
            space = True
        else:
            space = False
        temp = temp + x
    if stringa[0] == " ":
        temp = temp[1:]
    if stringa[-1] == " ":
        temp = temp[:-1]
    return temp.lower()


def descrizione_comando(comando, parola_chiave, parola_comando):
    comand = False
    temp = ""
    for x in range(comando.find(parola_chiave, comando.find(parola_comando) + len(parola_comando)), len(comando)):
        if comando[x] == ' ':
            comand = True
            continue
        if comand == True:
            temp += comando[x]
    return temp


def comandi(domanda, parola_chiave="", parola_comando=""):
    if domanda.find("informazioni") != -1 or domanda.find("informazione") != -1:
        parola_chiave = "su"
        parola_comando = "informazioni"
        if descrizione_comando(domanda, parola_chiave, parola_comando).find("professori") != -1:
            print(f"Hai chiesto informazzioni su {descrizione_comando(domanda,parola_chiave,parola_comando)}")
        else:
            print(f"Mi dispiace ma non so niente su {descrizione_comando(domanda,parola_chiave,parola_comando)}!!!")
            
    else if (domanda == "indicazioni") or (domanda == "Indicazioni"):
        print("Che tipo di indicazioni hai bisogno?")
        indicazionidomanda = input("Professori, classi, materiale didattico")
    elif (domanda == "aiuto") or (domanda == "Aiuto"):
        aiutodomanda = input("Con l'assistente, altro")
    else:
        print("Non ho capito di cosa hai bisogno")


comandi(extra_space_remover(input("Di cosa hai bisogno?  \n\n Indicazioni, informazioni, aiuto o altro\n-> ")))
