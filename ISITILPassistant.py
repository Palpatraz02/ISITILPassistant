
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
            inp = input("""Cosa vuoi sapere a rigurado?
            puoi sciengliere tra:
                I miei professori?
                Chi è il miglire?
                Chi è il peggiore?
                Quanti professori ci sono in questa scuola?
                    -> """)
            if inp.find("miei professori")!=-1 or inp.find("insegna"):
                inp = input("Mi serve sapre un ultima cosa.\nChe classe frequenti?\n ->")
                if inp.find("3 inf")!=-1:
                    print("Informazione attualmente non disponibile")
                else:
                    print("Mi dispiace ma non so niente su questa classe")
            else:
                print(f"Mi dispiace ma non so niente su {descrizione_comando(domanda,parola_chiave,parola_comando)}!!!")
            
        elif (domanda == "indicazioni") or (domanda == "Indicazioni"):
            print("Che tipo di indicazioni hai bisogno?")
            indicazionidomanda = input("Professori, classi, materiale didattico:\n -->")
            
            if indicazionidomanda.find("Professori") or ("prof") or ("professori")!=-1:
                nomeprofessore = input("Inserisci il nome di un prof oppure una classe in cui insegna oppure la materia\n -->")
               
                if nomeprofessore.find("Venturino") or ("venturino") !=-1:
                    print("Il prof "+ nomeprofessore + " insegna nelle classi:")
                    print("- 3 inf")
                    print("- 4 inf")
            
                else:
                    print("Il prof cercato non è disponibile o non esiste, ritenta")
    
            elif indicazionidomanda.find(indicazionidomanda == "Classi") or (indicazionidomanda == "classi")!=-1:
                inp2 = input("Mi serve sapre un ultima cosa.\nDi che classe hai bisogno?\n ->")
                if inp2.find("1 inf") or ("prima info") or ("prima informatica") or ("1 informatica")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("2 inf") or ("seconda info") or ("seconda informatica") or ("2 informatica")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("3 inf") or ("terza info") or ("terza informatica") or ("3 informatica")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("4 inf") or ("quarta info") or ("quarta informatica") or ("4 informatica")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("5 inf") or ("quinta info") or ("quinta informatica") or ("5 informatica")!=-1:
                    print("Informazione attualmente non disponibile")
                    
                elif inp2.find("1 ele") or ("prima ele") or ("prima elettronica") or ("1 elettronica")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("2 ele") or ("seconda ele") or ("seconda elettronica") or ("2 elettronica")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("3 ele") or ("terza ele") or ("terza elettronica") or ("3 elettronica") or ("terza elettronico") or ("3 elettronico")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("4 ele") or ("quarta ele") or ("quarta elettronica") or ("4 elettronica") or ("quarta elettronico") or ("4 elettronico")!=-1:
                    print("Informazione attualmente non disponibile")
                elif inp2.find("5 ele") or ("quinta ele") or ("quinta elettronica") or ("5 elettronica") or ("quinta elettronico") or ("5 elettronico")!=-1:
                    print("Informazione attualmente non disponibile")
            

            

  
        
        else:
            print("Non ho capito di cosa hai bisogno")


comandi(extra_space_remover(input("Di cosa hai bisogno?  \n\n Indicazioni, informazioni, aiuto o altro\n-> ")))

