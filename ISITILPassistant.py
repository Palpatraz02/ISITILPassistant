#prova Samuele
domanda = input("Di cosa hai bisogno?  /n/n Indicazioni, informazioni, aiuto o altro")

if (domanda == "indicazioni") or (domanda == "Indicazioni"):
  print("Che tipo di indicazioni hai bisogno?")
  indicazionidomanda = input("Professori, classi, materiale didattico")
#prova Fabien
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
def descrizione_comando(comando, parola_chiave):
    comand=False
    temp=""
    for x in range(comando.find(parola_chiave),len(comando)):
        if comando[x]==' ':
            comand = True
            continue
        if comand== True:
            temp+=comando[x]
    return temp
def comandi(comando, parola_chiave=""):
  if comando.find("informazioni")!=-1:
      parola_chiave="su"
      if descrizione_comando(comando,parola_chiave).find("professori")!=-1:
        print(f"Hai chiesto informazzioni su {descrizione_comando(comando,parola_chiave)}")
      else:
        print(f"Mi dispiace ma non so niente su {descrizione_comando(comando,parola_chiave)}!!!")
comandi(extra_space_remover(input("Di cosa hai bisogno?  \n\n Indicazioni, informazioni, aiuto o altro\n-> ")))
