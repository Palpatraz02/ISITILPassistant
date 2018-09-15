#prova Samuele
print("linea da cancellare")
domanda = input("Di cosa hai bisogno?  /n/n Indicazioni, informazioni, aiuto o altro")

if (domanda == "indicazioni") or (domanda == "Indicazioni"):
  print("Che tipo di indicazioni hai bisogno?")
  indicazionidomanda = input("Professori, classi, materiale didattico")
#prova Fabien
def descrizione_comando(comando):
    comand=False
    temp=""
    for x in comando:
        if x==' ':
            comand = True
            continue
        if comand== True:
            temp+=x
    return temp
def comandi(comando):
  if comando.find("indicazioni")!=-1:
      if descrizione_comando(comando).find("professori"):
        print(f"Ha chiesto informazzioni su {descrizione_comando(comando)}")
      else:
          print(f"Mi dispiace ma non so niente su {descrizione_comando(comando)}!!!")
comandi(input("-> "))
  
