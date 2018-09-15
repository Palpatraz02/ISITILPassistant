import Funzioni

def comandi(domanda):
    key_words=[]
    if domanda.find("non"):
        key_words.append("non")
    if Funzioni.memoria(domanda)==-1: Funzioni.impara(input("Non ho mai sentito questa domanda cosa devo riponere?\n ->"))
    else: print(Funzioni.memoria(domanda))

while True:
    comandi(Funzioni.rimuovi_spazzi_non_necessari(input("Di cosa hai bisogno?\n -> ")))
