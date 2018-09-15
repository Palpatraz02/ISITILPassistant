import Funzioni

def comandi(domanda):
    probabile_frase_negativa=False
    azione_sempre_vera=""
    azione_primaria=""
    parametri=[]
    if domanda.find("non")!=-1:
        probabile_frase_negativa=True
    if domanda.find("ciao") != -1:
        azione_sempre_vera="ciao"
    if domanda.find("informazioni")!=-1 or domanda.find("informazione")!=-1:
        azione_primaria="informazioni"
    if domanda.find("professori")!=-1 or domanda.find("professore")!=-1:
        parametri.append("professori")

    if probabile_frase_negativa==False:
        if azione_sempre_vera=="ciao":
            print("Caio!!")
        if azione_primaria=="informazioni":
            if len(parametri)!=0:
                for x in parametri:
                    if x == "professori":
                        print("Alloara hai chiesto informazzioni sui professori")
            else:
                print("Su cosa vuoi che ti informi")


    #if Funzioni.memoria(domanda)==-1: Funzioni.impara(input("Non ho mai sentito questa domanda cosa devo riponere?\n ->"))
    #else: print(Funzioni.memoria(domanda))

while True:
    comandi(Funzioni.rimuovi_spazzi_non_necessari(input("Di cosa hai bisogno?\n -> ")))
