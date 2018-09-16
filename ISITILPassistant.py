import Funzioni

def comandi(domanda):
    lista_materie=["italiano","matematica","francese","inglese","chimica","fisica","diritto"]
    lista_classi = [[1,2,3,4,5,"prima","seconda","terza","quarta","quinta"],["inf","ele","afm","oe","informatica","eletrronica","finanza e marketing","operatori elettrici"]]


    probabile_frase_negativa=False
    domanda_si_no = False
    azione_sempre_vera=""
    azione_primaria=""
    parametri=[]
    if domanda.find("non")!=-1:
        probabile_frase_negativa=True
    if domanda.find("vero") != -1:
        probabile_frase_negativa = True
    if domanda.find("ciao") != -1:
        azione_sempre_vera="ciao"
    if domanda.find("informazioni")!=-1 or domanda.find("informazione")!=-1:
        azione_primaria="informazioni"
    if domanda.find("professori")!=-1 or domanda.find("professore")!=-1:
        parametri.append("professori")
        for materia in lista_materie:
            if domanda.find(materia) != -1:
                parametri.append(materia)
        for indirizzo in lista_classi[1]:
            for classe in lista_classi[0]:
                if domanda.find(f"{classe} {indirizzo}")!=-1:
                    parametri.append(f"{classe} {indirizzo}")

    find=False
    find_materia = False
    print(parametri)
    if probabile_frase_negativa==False:
        if domanda_si_no==False:
            if azione_sempre_vera=="ciao":
                print("Ciao!!")
            if azione_primaria=="informazioni":
                if len(parametri)!=0:
                    if parametri[0] == "professori":
                        if len(parametri) >= 2:
                            for materia in lista_materie:
                                if parametri[1]==materia:
                                    find = True
                                    if len(parametri) >= 3:
                                        for indirizzo in lista_classi[1]:
                                            for classe in lista_classi[0]:
                                                if parametri[2] == f"{classe} {indirizzo}":
                                                    print(f"Mi dispice ma sono nuovo non so niente sui professori della {classe} {indirizzo} che insegnano {materia}")
                                                    find_materia = True
                                    if find_materia==False:
                                        print(f"Mi dispice ma sono nuovo non so niente sui professori di {materia}")
                            if find==False:
                                for indirizzo in lista_classi[1]:
                                    for classe in lista_classi[0]:
                                        if parametri[1]==f"{classe} {indirizzo}":
                                            print(f"Mi dispice ma sono nuovo non so niente sui professori della {classe} {indirizzo}")
                                            find=True
                        if find==False:
                            print("Alloara hai chiesto informazzioni sui professori")
                else:
                    print("Su cosa vuoi che ti informi")


    #if Funzioni.memoria(domanda)==-1: Funzioni.impara(input("Non ho mai sentito questa domanda cosa devo riponere?\n ->"))
    #else: print(Funzioni.memoria(domanda))

while True:
    comandi(Funzioni.rimuovi_spazzi_non_necessari(input("Di cosa hai bisogno?\n -> ")))
